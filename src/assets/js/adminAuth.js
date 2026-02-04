import { getSupabaseClient } from "./supabaseClient.js";

function qs(sel) {
  return document.querySelector(sel);
}

function setStatus(msg) {
  const el = qs("[data-status]");
  if (el) el.textContent = msg;
}

async function requireAuth() {
  const supabase = getSupabaseClient();
  if (!supabase) {
    setStatus("Missing SUPABASE_URL / SUPABASE_ANON_KEY environment variables.");
    return;
  }

  const { data } = await supabase.auth.getSession();
  if (!data.session) {
    window.location.href = "/admin/login/";
  }
}

async function initLogin() {
  const supabase = getSupabaseClient();
  if (!supabase) {
    setStatus("Missing SUPABASE_URL / SUPABASE_ANON_KEY environment variables.");
    return;
  }

  const form = qs("form[data-login]");
  if (!form) return;

  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    setStatus("Signing in…");

    const email = qs("#email")?.value?.trim();
    const password = qs("#password")?.value;

    const { error } = await supabase.auth.signInWithPassword({ email, password });
    if (error) {
      setStatus(error.message);
      return;
    }

    window.location.href = "/admin/dashboard/";
  });
}

async function initLogout() {
  const supabase = getSupabaseClient();
  const btn = qs("[data-logout]");
  if (!btn || !supabase) return;

  btn.addEventListener("click", async () => {
    await supabase.auth.signOut();
    window.location.href = "/admin/login/";
  });
}

(async function main() {
  const pageType = document.documentElement.getAttribute("data-admin-page");

  if (pageType === "login") {
    await initLogin();
    return;
  }

  if (pageType && pageType.startsWith("admin:")) {
    await requireAuth();
    await initLogout();
  }
})();
