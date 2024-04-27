import * as baseComponents from '.';

declare module '@vue/runtime-core' {
  export interface GlobalComponents {
    ABtnDark: typeof baseComponents.ABtnDark;
  }
}
