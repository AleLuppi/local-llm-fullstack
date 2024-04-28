import { boot } from 'quasar/wrappers';

import * as baseComponents from 'src/components/base';

/**
 * Register components from the base directory.
 */
export default boot(async ({ app }) => {
  Object.entries(baseComponents).forEach(([componentName, component]) =>
    app.component(componentName, component)
  );
});
