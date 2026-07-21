import adapter from '@sveltejs/adapter-static';
import { vitePreprocess } from '@sveltejs/vite-plugin-svelte';

/** @type {import('@sveltejs/kit').Config} */
const config = {
  preprocess: vitePreprocess(),
  kit: {
    adapter: adapter({ strict: false }),
    prerender: {
      crawl: true,
      entries: ['*'],
      handleHttpError: ({ status, path }) => {
        if (status === 404 && /^\/crystal-core\/|^\/[a-z-]*\/$/.test(path)) {
          return;
        }
        throw new Error(`${status} ${path}`);
      }
    }
  }
};

export default config;
