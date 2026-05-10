import crypto from "node:crypto";

import { cookies } from "next/headers";

const SETTINGS_COOKIE = "stock_settings_session";
const SESSION_TTL_SECONDS = 60 * 60 * 8;

function getSettingsPassword() {
  return process.env.SETTINGS_PASSWORD?.trim() ?? "";
}

function getSessionSecret() {
  return process.env.SETTINGS_SESSION_SECRET?.trim() || getSettingsPassword();
}

function createSessionToken() {
  const password = getSettingsPassword();
  const secret = getSessionSecret();
  if (!password || !secret) {
    return "";
  }

  return crypto.createHash("sha256").update(`${password}:${secret}`).digest("hex");
}

function equalText(left: string, right: string) {
  const leftBuffer = Buffer.from(left);
  const rightBuffer = Buffer.from(right);
  return leftBuffer.length === rightBuffer.length && crypto.timingSafeEqual(leftBuffer, rightBuffer);
}

export function isSettingsPasswordConfigured() {
  return Boolean(getSettingsPassword());
}

export function verifySettingsPassword(password: string) {
  const expectedPassword = getSettingsPassword();
  return Boolean(expectedPassword) && equalText(password.trim(), expectedPassword);
}

export async function hasSettingsAccess() {
  if (!isSettingsPasswordConfigured() && process.env.NODE_ENV !== "production") {
    return true;
  }

  const expectedToken = createSessionToken();
  const actualToken = (await cookies()).get(SETTINGS_COOKIE)?.value ?? "";
  return Boolean(expectedToken) && equalText(actualToken, expectedToken);
}

export async function setSettingsSession() {
  (await cookies()).set(SETTINGS_COOKIE, createSessionToken(), {
    httpOnly: true,
    maxAge: SESSION_TTL_SECONDS,
    path: "/settings",
    sameSite: "lax",
    secure: process.env.NODE_ENV === "production"
  });
}

export async function clearSettingsSession() {
  (await cookies()).set(SETTINGS_COOKIE, "", {
    httpOnly: true,
    maxAge: 0,
    path: "/settings",
    sameSite: "lax",
    secure: process.env.NODE_ENV === "production"
  });
}
