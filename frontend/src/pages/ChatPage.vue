<template>
  <q-page class="column">
    <!-- Display current chat history -->
    <q-list class="col q-px-lg q-py-md">
      <q-item
        v-for="(message, idx) in chatHistory"
        :key="idx"
        class="items-start"
      >
        <q-item-section avatar>
          <q-avatar color="primary" icon="person" size="sm" />
        </q-item-section>

        <q-item-label style="white-space: pre; font-size: 1.1em">
          {{ message }}
        </q-item-label>
      </q-item>
    </q-list>

    <!-- Display chat input -->
    <div class="chat-elements q-px-md">
      <input-llm-message v-model="chatMessage" @submit="chatSubmit" />
    </div>
  </q-page>
</template>

<script setup lang="ts">
import { defineAsyncComponent } from 'vue';
import { useLlmChat } from 'src/composables/llmChat';

// Import components
const InputLlmMessage = defineAsyncComponent(
  () => import('src/components/InputLlmMessage.vue'),
);

const { chatMessage, chatHistory, submit: chatSubmit } = useLlmChat();
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
