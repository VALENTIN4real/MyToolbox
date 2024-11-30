export default {
  install(app) {
    app.config.globalProperties.$env = {
      API_URL: import.meta.env.VITE_API_URL,
    };
  },
};
