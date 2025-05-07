import { defineBoot } from '#q-app/wrappers';

import * as baseComponents from 'components/base';

/**
 * Register components from the base directory.
 */
export default defineBoot(({ app }) => {
  Object.entries(baseComponents).forEach(([componentName, component]) =>
    app.component(componentName, component),
  );
});
