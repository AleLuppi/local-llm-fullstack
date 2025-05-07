<template>
  <q-drawer v-bind="$props" v-model="modelValue">
    <div class="column justify-between full-height">
      <list-chat-history
        :chats="dateSortedChats"
        :title="$t('chat.history.title')"
        open-chat
        new-chat
        class="col q-pa-md"
      />

      <div class="row justify-between q-pa-sm">
        <a-btn-dark size="sm" outline outline-color="grey" />

        <a-btn size="sm" :label="$t('locale.name')" outline outline-color="grey" />
      </div>
    </div>
  </q-drawer>
</template>

<script setup lang="ts">
import { defineAsyncComponent, onMounted } from 'vue';
import { type QDrawerProps, QDrawer } from 'quasar';
import { storeToRefs } from 'pinia';
import { useChatHistoryStore } from 'src/stores/chatHistoryStore';

// Import components
const ListChatHistory = defineAsyncComponent(() => import('src/components/ListChatHistory.vue'));

// Define props
// eslint-disable-next-line vue/prop-name-casing
withDefaults(defineProps<Omit<QDrawerProps, 'modelValue'>>(), { dark: undefined });

// Define model
const modelValue = defineModel<QDrawerProps['modelValue']>({
  default: undefined,
});

// Retrieve chat history
const chatHistoryStore = useChatHistoryStore();
const { dateSortedChats } = storeToRefs(chatHistoryStore);

// Load chat history on mount
onMounted(chatHistoryStore.loadChats);
</script>
