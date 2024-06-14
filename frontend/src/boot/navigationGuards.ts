import { boot } from 'quasar/wrappers';

/**
 * Set up global router navigation guards.
 */
export default boot(async ({ router }) => {
  router.beforeEach(async (to) => {
    // Remove (normalize) empty params
    Object.keys(to.params).forEach((key) => {
      if (!to.params[key]) delete to.params[key];
    });
  });
});
