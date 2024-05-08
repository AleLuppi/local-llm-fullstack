<template>
  <q-page class="column">
    <!-- Display current chat history -->
    <q-list class="col q-px-lg q-py-md full-width">
      <q-item
        v-for="(message, idx) in allChatMessages"
        :key="idx"
        class="items-start"
      >
        <q-item-section avatar>
          <q-avatar color="primary" icon="person" size="sm" />
        </q-item-section>

        <q-item-label class="text-pre-wrap-break col" style="font-size: 1.1em">
          {{ message }}
        </q-item-label>
      </q-item>
    </q-list>

    <!-- Display chat input -->
    <div class="chat-elements q-px-md">
      <input-agent-message v-model="chatMessage" @submit="chatSubmit" />
    </div>
  </q-page>
</template>

<script setup lang="ts">
import { defineAsyncComponent } from 'vue';
import { useAgentChat } from 'src/composables/agentChat';

// Import components
const InputAgentMessage = defineAsyncComponent(
  () => import('src/components/InputAgentMessage.vue'),
);

// Get refs
const {
  chatMessage,
  allChatMessages,
  isLoading: waitingAgent,
  loadingMessage,
  submit: chatSubmit,
} = useAgentChat();
</script>

<style scoped lang="scss">
.chat-elements {
  position: sticky;
  bottom: 10px;
}

.input-chat:deep(textarea) {
  max-height: min(20vh, 500px, 20em);
}
</style>
