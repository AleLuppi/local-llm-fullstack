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
        :bg-color="$q.dark.isActive ? 'dark' : 'white'"
        @keydown.enter="multiLineMessage ? undefined : onSubmit()"
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
      <div v-show="showChatConfig">
        <q-separator size="8px" color="transparent" />
        <q-card
          flat
          bordered
          class="row q-mx-auto"
          style="border-radius: 8px; max-width: 80%"
        >
          <span class="col-12 q-pt-sm q-px-sm text-small">
            {{ $t('chat.messageConfig') }}
          </span>
          <q-checkbox
            v-model="multiLineMessage"
            :label="$t('chat.messageMultiline')"
            :checked-icon="fasAlignLeft"
            :unchecked-icon="fasAlignLeft"
            :class="{ 'text-grey': !multiLineMessage }"
          />
        </q-card>
      </div>
    </q-slide-transition>
  </div>
</template>

<script setup lang="ts">
import { ref, watch } from 'vue';
import {
  fasAlignLeft,
  fasAngleDown,
  fasAngleUp,
  fasTurnUp,
} from '@quasar/extras/fontawesome-v6';

// Define props
const props = defineProps<{
  // preserve model value on message submit
  preserveOnSubmit?: boolean;

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

// Whether message is multiline
const multiLineMessage = ref(false);

// Ensure model value does not include newlines if message is single line
watch(modelValue, (val) => {
  if (!multiLineMessage.value) modelValue.value = val?.replace(/\n/g, '');
});

/**
 * Submit chat message.
 */
function onSubmit() {
  if (modelValue.value?.trim()) emit('submit', modelValue.value);

  if (!props.preserveOnSubmit) modelValue.value = '';
}
</script>
