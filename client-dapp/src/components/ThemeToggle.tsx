'use client'
import { useEffect, useState } from 'react'

export default function ThemeToggle() {
  const [isDark, setIsDark] = useState(false)

  useEffect(() => {
    const storedTheme = localStorage.getItem('theme')
    const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches
    const enabledDark = storedTheme === 'dark' || (!storedTheme && prefersDark)
    setTheme(enabledDark)
  }, [])

  const setTheme = (dark: boolean) => {
    const root = document.documentElement
    if (dark) {
      root.style.setProperty('--background', '#0a0a0a')
      root.style.setProperty('--foreground', '#ededed')
      localStorage.setItem('theme', 'dark')
    } else {
      root.style.setProperty('--background', '#ffffff')
      root.style.setProperty('--foreground', '#171717')
      localStorage.setItem('theme', 'light')
    }
    setIsDark(dark)
  }

  return (
    <button
      onClick={() => setTheme(!isDark)}
      className="fixed top-4 right-4 z-50 px-3 py-1 rounded bg-gray-300 text-black"
    >
      {isDark ? '☀️ Light' : '🌙 Dark'}
    </button>
  )
}
