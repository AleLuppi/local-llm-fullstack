<template>
  <q-page class="column">
    <!-- Display current chat history -->
    <list-chat-messages
      :messages="allChatMessages"
      :waiting="waitingAgent"
      :waiting-message="waitingAgentMessage"
      class="col q-px-lg q-py-md"
    />

    <!-- Display chat input -->
    <div class="chat-elements q-px-md q-pb-md q-pt-sm glass">
      <input-agent-message v-model="chatMessage" @submit="chatSubmit" />
    </div>
  </q-page>
</template>

<script setup lang="ts">
import { defineAsyncComponent, watch } from 'vue';
import { useRoute } from 'vue-router';
import { storeToRefs } from 'pinia';
import { useAgentChat } from 'src/composables/agentChat';
import { useChatHistoryStore } from 'src/stores/chatHistoryStore';

// Import components
const ListChatMessages = defineAsyncComponent(
  () => import('src/components/ListChatMessages.vue'),
);
const InputAgentMessage = defineAsyncComponent(
  () => import('src/components/InputAgentMessage.vue'),
);

// Get route
const route = useRoute();

// Get refs
const {
  chatMessage,
  allChatMessages,
  chatReference,
  isLoading: waitingAgent,
  loadingMessage: waitingAgentMessage,
  submit: chatSubmit,
} = useAgentChat();

// Retrieve chat history
const chatHistoryStore = useChatHistoryStore();
const { dateSortedChats } = storeToRefs(chatHistoryStore);

// Retrieve requested chat
watch(
  [() => route.params.id, dateSortedChats],
  () => {
    chatReference.value = chatHistoryStore.getChat(route.params.id as string);
  },
  { immediate: true },
);
</script>

<style scoped lang="scss">
.chat-elements {
  position: sticky;
  bottom: 0;
}

.input-chat:deep(textarea) {
  max-height: min(20vh, 500px, 20em);
}
</style>
