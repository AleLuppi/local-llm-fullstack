<template>
  <q-list>
    <q-item
      v-for="({ role, message }, idx) in displayMessages"
      :key="idx"
      class="items-start q-py-md"
    >
      <q-item-section avatar>
        <q-avatar
          :color="role == ChatRole.agent ? ($q.dark.isActive ? 'white' : 'black') : 'primary'"
          :text-color="role == ChatRole.agent && $q.dark.isActive ? 'black' : 'white'"
          :icon="role == ChatRole.agent ? fasRobot : fasUserAstronaut"
          size="sm"
        />
      </q-item-section>

      <q-item-label
        class="text-pre-wrap-break col q-pt-xs"
        :class="{
          'text-bold text-italic': waiting && idx == messages.length && role == ChatRole.agent,
        }"
        style="font-size: 1.1em"
      >
        {{ message }}
      </q-item-label>
    </q-item>
  </q-list>
</template>

<script setup lang="ts">
import { computed } from 'vue';
import { useQuasar } from 'quasar';
import { type ChatMessage, ChatRole } from 'src/models/chat';
import { fasRobot, fasUserAstronaut } from '@quasar/extras/fontawesome-v6';

// Define props
const props = defineProps<{
  // list of chat messages to display
  messages: ChatMessage[];

  // whether agent is generating a response
  waiting?: boolean;

  // Optional text to display while waiting for agent response
  waitingMessage?: string;
}>();

// Init plugin
const $q = useQuasar();

// Prepare messages to display
const displayMessages = computed(() =>
  props.messages
    .map((message) => {
      return { message: message.content, role: message.role };
    })
    .concat(props.waiting ? [{ message: props.waitingMessage ?? '', role: ChatRole.agent }] : []),
);
</script>
