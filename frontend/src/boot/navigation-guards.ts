import { defineBoot } from '#q-app/wrappers';

/**
 * Set up global router navigation guards.
 */
export default defineBoot(({ router }) => {
  router.beforeEach((to) => {
    // Remove (normalize) empty params
    Object.keys(to.params).forEach((key) => {
      if (!to.params[key]) delete to.params[key];
    });
  });
});
