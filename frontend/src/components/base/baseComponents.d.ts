import * as baseComponents from '.';

declare module '@vue/runtime-core' {
  export interface GlobalComponents {
    ABtn: typeof baseComponents.ABtn;
    ABtnDark: typeof baseComponents.ABtnDark;
  }
}

/**********************/
/***** INTERFACES *****/
/**********************/
import type { QBtnProps } from 'quasar';

export interface ABtnProps extends QBtnProps {
  outlineColor?: string;
}

// eslint-disable-next-line @typescript-eslint/no-empty-interface
export interface ABtnDarkProps extends Omit<ABtnProps, 'icon'> {}
