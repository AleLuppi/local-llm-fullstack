<template>
  <q-list>
    <q-item-label v-if="title" header> {{ title }} </q-item-label>

    <q-item
      v-for="chat in chats"
      :key="chat.uid"
      :clickable="openChat"
      @click="
        openChat
          ? $router.push({ name: PageName.chat, params: { uid: chat.uid } })
          : undefined
      "
    >
      <q-item-section>
        <q-item-label>
          {{
            chat.summary ??
            (chat.creationDate
              ? $t('chat.history.chatFromDate') + $d(chat.creationDate)
              : 'Hello')
          }}
        </q-item-label>
      </q-item-section>
    </q-item>
  </q-list>
</template>

<script setup lang="ts">
import type { Chat } from 'src/models/chat';
import { PageName } from 'src/router';

// Define props
defineProps<{
  // list of chats to display
  chats: Chat[];

  // optional title
  title?: string;

  // whether to navigate to chat on click
  openChat?: boolean;
}>();
</script>
