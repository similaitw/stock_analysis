"use client";

import { useEffect, useState } from "react";

type SkinId = "cedar" | "graphite" | "jade" | "harbor" | "crimson";

const SKINS: Array<{
  id: SkinId;
  label: string;
  swatch: string;
}> = [
  { id: "cedar", label: "暖木", swatch: "#9c4f22" },
  { id: "graphite", label: "石墨", swatch: "#475569" },
  { id: "jade", label: "青玉", swatch: "#0f766e" },
  { id: "harbor", label: "港灣", swatch: "#2563eb" },
  { id: "crimson", label: "酒紅", swatch: "#be123c" }
];

const STORAGE_KEY = "stock-analysis-skin";
const DEFAULT_SKIN: SkinId = "cedar";

function isSkinId(value: string | null): value is SkinId {
  return Boolean(value && SKINS.some((skin) => skin.id === value));
}

function getInitialSkin(): SkinId {
  if (typeof window === "undefined") {
    return DEFAULT_SKIN;
  }

  const storedSkin = window.localStorage.getItem(STORAGE_KEY);
  if (isSkinId(storedSkin)) {
    return storedSkin;
  }

  const documentSkin = document.documentElement.dataset.skin ?? null;
  return isSkinId(documentSkin) ? documentSkin : DEFAULT_SKIN;
}

export function SkinSwitcher() {
  const [activeSkin, setActiveSkin] = useState<SkinId>(getInitialSkin);

  useEffect(() => {
    document.documentElement.dataset.skin = activeSkin;
    window.localStorage.setItem(STORAGE_KEY, activeSkin);
  }, [activeSkin]);

  function chooseSkin(skin: SkinId) {
    setActiveSkin(skin);
  }

  return (
    <div className="skin-switcher" aria-label="介面 skin 選擇" suppressHydrationWarning>
      <span>Skin</span>
      <div className="skin-options">
        {SKINS.map((skin) => (
          <button
            key={skin.id}
            type="button"
            className={activeSkin === skin.id ? "skin-option active" : "skin-option"}
            onClick={() => chooseSkin(skin.id)}
            aria-label={`切換到${skin.label} skin`}
            title={skin.label}
          >
            <span style={{ background: skin.swatch }} />
          </button>
        ))}
      </div>
    </div>
  );
}
