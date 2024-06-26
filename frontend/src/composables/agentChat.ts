import { computed, onUnmounted, ref, watch } from 'vue';
import { useI18n } from 'vue-i18n';
import { requestAgentAnswer } from 'src/api/apiAgent';
import { Chat, ChatMessage, ChatRole } from 'src/models/chat';
import { useChatHistoryStore } from 'src/stores/chatHistoryStore';

export function useAgentChat() {
  // Init plugin
  const { t } = useI18n();

  // User chat message
  const chatMessage = ref('');

  // Current chat
  const chatReference = ref<Chat>();

  // Waiting for LLM response
  const isLoading = ref(false);
  const loadingMessage = ref('');

  // Catch error status on last message
  const isError = ref(false);

  // Check how many pending chats are present
  const countLoading = ref(0);

  // Current chat history of messages
  const allChatMessages = computed<ChatMessage[]>(
    () => chatReference.value?.messages ?? [],
  );

  // Get method to update chat history
  const { updateChat } = useChatHistoryStore();

  /**
   * Submit message and send it to LLM.
   *
   * @param {string} text - Optional message to override chat model value.
   */
  function submit(text?: string) {
    // Cleanup input message
    chatMessage.value = '';

    // Set loading and error state
    isLoading.value = true;
    isError.value = false;
    countLoading.value++;

    // Create or update chat
    requestAgentAnswer(chatReference.value, text)
      .then((response) => {
        updateChat(response);

        // Update current chat if it's same chat or last one waiting for answer
        if (
          chatReference.value &&
          (chatReference.value.uid == response.uid ||
            (!chatReference.value.uid && countLoading.value == 1))
        )
          chatReference.value = response;
      })
      .catch(() => {
        isError.value = true;
      })
      .finally(() => {
        isLoading.value = false;
        countLoading.value = Math.max(countLoading.value - 1, 0);
      });

    // Build a temporary chat while waiting for LLM response
    if (!chatReference.value)
      chatReference.value = new Chat({ uid: '', messages: [] });
    chatReference.value.append(
      new ChatMessage({
        role: ChatRole.user,
        content: text ?? chatMessage.value,
      }),
    );
  }

  // Clear state if a new chat is opened
  watch(chatReference, (currChat, prevChat) => {
    if (!currChat || (currChat.uid && currChat.uid !== prevChat?.uid)) {
      isLoading.value = false;
      isError.value = false;
    }
  });

  // Build a waiting message when loading answer from agent
  let interval: ReturnType<typeof setInterval> | undefined;
  watch(isLoading, (loading) => {
    if (loading) {
      loadingMessage.value = t('chat.message.agentWaitingMessage');
      interval = setInterval(() => {
        loadingMessage.value += '.';
        if (loadingMessage.value.endsWith('....'))
          loadingMessage.value = loadingMessage.value.slice(0, -4);
      }, 500);
    } else {
      if (interval) clearInterval(interval);
    }
  });

  // Clear interval when component is unmounted
  onUnmounted(() => {
    if (interval) clearInterval(interval);
  });

  return {
    chatMessage,
    chatReference,
    allChatMessages,
    isLoading,
    loadingMessage,
    isError,
    submit,
  };
}
