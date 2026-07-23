<script>
  import Footer from '$lib/components/Footer.svelte';

  let { data } = $props();
</script>

<svelte:head>
  <title>Protocols — TerAustralis Incognita</title>
</svelte:head>

<section class="section node" style="--node:var(--green)">
  <h2>Protocols</h2>
  <p>
    The technical layer — each entry carries its status and the code to verify it. What is
    <strong>Built</strong> has a self-test you can run; what is <strong>Design</strong> says so
    plainly.
  </p>
</section>

<section class="section node" style="--node:var(--blue)">
  <h2>The stack</h2>
  <div class="cards">
    {#each data.protocols as p (p.title)}
      <div class="card" style="--st:{p.st}">
        <h3>{p.title}</h3>
        <span class="status">{p.status}</span>
        <p>{p.body}</p>
        <p>
          {#each p.links as link, i (link.href)}{#if i > 0} · {/if}<a href={link.href}>{link.label}</a>{/each}
        </p>
      </div>
    {/each}
  </div>
</section>

<Footer />
