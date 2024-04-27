import { ref } from 'vue';

export function useLlmChat() {
  // User chat message
  const chatMessage = ref('');

  // Current chat history
  const chatHistory = ref<string[]>([]);

  /**
   * Submit message and send it to LLM.
   *
   * @param {string} text - Optional message to override chat model value.
   */
  function submit(text?: string) {
    chatHistory.value.push(text ?? chatMessage.value);
    chatMessage.value = '';

    // TODO send to LLM
  }

  return {
    chatMessage,
    chatHistory,
    submit,
  };
}
