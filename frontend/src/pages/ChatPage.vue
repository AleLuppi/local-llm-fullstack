<template>
  <q-page class="column" style="padding-top: 50px">
    <q-page-sticky
      position="top"
      expand
      class="glass text-inherit q-header q-header--bordered"
    >
      <toolbar-agent-info />
    </q-page-sticky>

    <!-- Display current chat history -->
    <list-chat-messages
      :messages="allChatMessages"
      :waiting="waitingAgent"
      :waiting-message="waitingAgentMessage"
      class="col q-px-lg q-py-md"
    />

    <!-- Display chat input -->
    <div class="chat-elements q-px-md q-pb-md q-pt-sm glass">
      <input-agent-message
        v-model="chatMessage"
        :loading="waitingAgent"
        @submit="onSubmit"
      />
    </div>
  </q-page>
</template>

<script setup lang="ts">
import { defineAsyncComponent, watch } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { PageName } from 'src/router';
import { useAgentChat } from 'src/composables/agentChat';
import { useChatHistoryStore } from 'src/stores/chatHistoryStore';

// Import components
const ToolbarAgentInfo = defineAsyncComponent(
  () => import('src/components/ToolbarAgentInfo.vue'),
);
const ListChatMessages = defineAsyncComponent(
  () => import('src/components/ListChatMessages.vue'),
);
const InputAgentMessage = defineAsyncComponent(
  () => import('src/components/InputAgentMessage.vue'),
);

// Get router
const route = useRoute();
const router = useRouter();

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

// Retrieve requested chat
watch(
  [() => route.params.id as string | undefined, () => route.query.status],
  ([currId, currStatus], [, prevStatus]) => {
    // Skip chat load if just setting a new internal status
    if (currStatus != prevStatus && currStatus) return;

    // Open requested chat
    chatReference.value = currId ? chatHistoryStore.getChat(currId) : undefined;

    // Delete chat ID from url if chat does not exist
    if (!chatReference.value) router.replace({ name: PageName.chat });
  },
  { immediate: true },
);

// Ensure chat id param matches current opened chat
watch(
  () => chatReference.value?.uid,
  (newId) => {
    if (newId || newId === undefined)
      router.replace({ name: PageName.chat, params: { id: newId } });
  },
);

/**
 * Manage chat message submit.
 *
 * @param {string} message - The user chat message to be submitted.
 */
function onSubmit(message: string) {
  // If new chat is being submitted, add a query param to route
  // to notify this, so that a new chat may optionally be opened
  if (route.params.id == undefined)
    router.push({ name: PageName.chat, query: { status: 'new' } });

  // Actually submit message
  chatSubmit(message);
}
</script>

<style scoped lang="scss">
.chat-elements {
  position: sticky;
  bottom: 0;
}
</style>
