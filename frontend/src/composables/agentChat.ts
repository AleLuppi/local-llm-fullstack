import { computed, onUnmounted, ref, watch } from 'vue';
import { useI18n } from 'vue-i18n';
import { requestAgentAnswer } from 'src/api/apiAgent';
import { Chat, ChatMessage, ChatRole } from 'src/models/chat';

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

  // Current chat history of messages
  const allChatMessages = computed<string[]>(
    () => chatReference.value?.messages.map((message) => message.content) ?? [],
  );

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

    // Create or update chat
    requestAgentAnswer(chatReference.value, text)
      .then((response) => {
        chatReference.value = response;
      })
      .catch(() => (isError.value = true))
      .finally(() => {
        isLoading.value = false;
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

  // Build a waiting message when loading answer from agent
  let interval: ReturnType<typeof setInterval> | undefined;
  watch(isLoading, (loading) => {
    if (loading) {
      loadingMessage.value = t('chat.messageWaitingAgent');
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
