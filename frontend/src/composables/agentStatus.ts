import { onMounted, onUnmounted, ref } from 'vue';
import { isHealthy } from 'src/api/apiAgent';

export function useAgentStatus() {
  // Store agent status
  const agentConnected = ref(false);

  /**
   * Check agent status and store it.
   */
  function checkAgentStatus() {
    isHealthy().then((status) => (agentConnected.value = status));
  }

  // Periodically check agent status
  let intervalId: ReturnType<typeof setInterval> | undefined;
  onMounted(() => {
    intervalId = setInterval(checkAgentStatus, 1000);
  });

  // Dismiss agent status check
  onUnmounted(() => {
    clearInterval(intervalId);
  });

  return {
    agentConnected,
  };
}
