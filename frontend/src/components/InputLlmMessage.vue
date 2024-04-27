<template>
  <div>
    <div class="row items-center full-width q-col-gutter-md">
      <div v-if="!hideChatConfig">
        <a-btn
          :color="$q.dark.isActive ? 'grey-9' : 'grey-4'"
          :icon="showChatConfig ? fasAngleUp : fasAngleDown"
          unelevated
          :padding="`${showChatConfig ? 3 : 5}px 4px ${
            showChatConfig ? 5 : 3
          }px 4px`"
          size="sm"
          style="border-radius: 8px"
          @click="showChatConfig = !showChatConfig"
        />
      </div>
      <q-input
        v-model="modelValue"
        autogrow
        outlined
        :placeholder="$t('chat.messagePlaceholder')"
        class="input-chat col"
        @keyup.enter="onSubmit"
      />
      <div>
        <a-btn
          color="primary"
          :icon="fasTurnUp"
          unelevated
          padding="8px 7px 8px 9px"
          style="border-radius: 8px"
          @click="onSubmit"
        />
      </div>
    </div>

    <q-slide-transition v-if="!hideChatConfig">
      <div v-show="showChatConfig" class="row q-px-lg">
        <!-- TODO add chat config elements -->
      </div>
    </q-slide-transition>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import {
  fasAngleDown,
  fasAngleUp,
  fasTurnUp,
} from '@quasar/extras/fontawesome-v6';

// Define props
const props = defineProps<{
  // clear model value on message submit
  clearOnSubmit?: boolean;

  // do not allow chat config
  hideChatConfig?: boolean;
}>();

// Define emits
const emit = defineEmits<{
  submit: [message: string];
}>();

// Define model
const modelValue = defineModel<string>();

// Whether to show helper buttons
const showChatConfig = ref(false);

/**
 * Submit chat message.
 */
function onSubmit() {
  if (modelValue.value?.trim()) emit('submit', modelValue.value);

  if (props.clearOnSubmit) modelValue.value = '';
}
</script>
