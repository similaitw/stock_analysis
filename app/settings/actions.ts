"use server";

import { redirect } from "next/navigation";

import { clearSettingsSession, setSettingsSession, verifySettingsPassword } from "@/lib/settings-auth";

export async function unlockSettings(formData: FormData) {
  const password = String(formData.get("password") ?? "");

  if (!verifySettingsPassword(password)) {
    redirect("/settings?auth=failed");
  }

  await setSettingsSession();
  redirect("/settings");
}

export async function lockSettings() {
  await clearSettingsSession();
  redirect("/");
}
