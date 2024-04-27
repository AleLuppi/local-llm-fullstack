<template>
  <q-drawer v-bind="$props" v-model="modelValue">
    <div class="column justify-between full-height">
      <q-scroll-area class="col">
        <q-list>
          <q-item-label header> {{ $t('chat.historyTitle') }} </q-item-label>
        </q-list>
      </q-scroll-area>

      <div class="row justify-between q-pa-sm">
        <a-btn-dark size="sm" outline outline-color="grey" />

        <a-btn
          size="sm"
          :label="$t('locale.name')"
          outline
          outline-color="grey"
        />
      </div>
    </div>
  </q-drawer>
</template>

<script setup lang="ts">
import { type QDrawerProps, QDrawer } from 'quasar';

// Define props
withDefaults(defineProps<QDrawerProps>(), { dark: undefined });

// Define model
const modelValue = defineModel<QDrawerProps['modelValue']>({
  default: undefined,
});
</script>
