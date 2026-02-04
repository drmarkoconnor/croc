import { createClient } from "@supabase/supabase-js";

export function getSupabaseClient() {
  const url = import.meta?.env?.SUPABASE_URL || process.env.SUPABASE_URL;
  const anonKey = import.meta?.env?.SUPABASE_ANON_KEY || process.env.SUPABASE_ANON_KEY;

  if (!url || !anonKey) {
    return null;
  }

  return createClient(url, anonKey);
}
