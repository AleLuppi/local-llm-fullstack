<template>
  <div class="column">
    <q-btn
      v-if="newChat"
      outline
      no-caps
      :ripple="false"
      class="full-width q-mb-lg"
      @click="$router.push({ name: PageName.chat })"
    >
      <div class="col row justify-evenly items-center">
        {{ $t('chat.history.newChat') }}
        <q-icon :name="farPenToSquare" size="xs" />
      </div>
    </q-btn>

    <q-scroll-area class="col" content-style="width: 100%">
      <q-list>
        <q-item-label v-if="title" header class="q-px-none">
          {{ title }}
        </q-item-label>

        <q-item
          v-for="chat in chats"
          :key="chat.uid"
          :clickable="openChat"
          @click="
            openChat
              ? $router.push({ name: PageName.chat, params: { id: chat.uid } })
              : undefined
          "
        >
          <q-item-section>
            <q-item-label
              style="
                white-space: nowrap;
                overflow-x: hidden;
                text-overflow: ellipsis;
              "
            >
              {{
                chat.summary ??
                (chat.creationDate
                  ? $t('chat.history.chatFromDate') + $d(chat.creationDate)
                  : $t('chat.history.chatUnknown'))
              }}
            </q-item-label>
          </q-item-section>
        </q-item>
      </q-list>
    </q-scroll-area>
  </div>
</template>

<script setup lang="ts">
import type { Chat } from 'src/models/chat';
import { PageName } from 'src/router';
import { farPenToSquare } from '@quasar/extras/fontawesome-v6';

// Define props
defineProps<{
  // list of chats to display
  chats: Chat[];

  // optional title
  title?: string;

  // whether to show button to open a new chat
  newChat?: boolean;

  // whether to navigate to chat on click
  openChat?: boolean;
}>();
</script>
