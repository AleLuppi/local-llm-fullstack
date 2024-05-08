<template>
  <q-page class="column">
    <!-- Display current chat history -->
    <q-list class="col q-px-lg q-py-md full-width">
      <q-item
        v-for="(
          { role, content: message }, idx
        ) in chatReference?.messages.concat(
          waitingAgent
            ? [{ role: ChatRole.agent, content: loadingMessage }]
            : [],
        )"
        :key="idx"
        class="items-start q-py-md"
      >
        <q-item-section avatar>
          <q-avatar
            :color="
              role == ChatRole.agent
                ? $q.dark.isActive
                  ? 'white'
                  : 'black'
                : 'primary'
            "
            :text-color="
              role == ChatRole.agent && $q.dark.isActive ? 'black' : 'white'
            "
            :icon="role == ChatRole.agent ? fasRobot : fasUserAstronaut"
            size="sm"
          />
        </q-item-section>

        <q-item-label
          class="text-pre-wrap-break col q-pt-xs"
          :class="{
            'text-bold text-italic':
              waitingAgent &&
              idx == chatReference?.messages.length &&
              role == ChatRole.agent,
          }"
          style="font-size: 1.1em"
        >
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
import { useQuasar } from 'quasar';
import { useAgentChat } from 'src/composables/agentChat';
import { ChatRole } from 'src/models/chat';
import { fasRobot, fasUserAstronaut } from '@quasar/extras/fontawesome-v6';

// Import components
const InputAgentMessage = defineAsyncComponent(
  () => import('src/components/InputAgentMessage.vue'),
);

// Init plugin
const $q = useQuasar();

// Get refs
const {
  chatMessage,
  chatReference,
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
