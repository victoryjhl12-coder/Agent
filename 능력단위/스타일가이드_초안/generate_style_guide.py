import os
import subprocess
import tempfile
import time
from pathlib import Path

BASE_DIR = Path(r"C:\Users\SBS\Documents\GitHub\0820_test")
OUTPUT_DIR = BASE_DIR / "스타일가이드_초안"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
if not os.path.exists(CHROME_PATH):
    CHROME_PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

COMMON_CSS = """
@import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard-dynamic-subset.min.css');
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600;700;800&family=Plus+Jakarta+Sans:wght@500;600;700;800&family=Inter:wght@400;500;600;700&display=swap');

:root {
  --bg-canvas: #090D16;
  --bg-surface-1: #111827;
  --bg-surface-2: #1F2937;
  --bg-surface-3: #283548;
  --primary: #6366F1;
  --primary-hover: #4F46E5;
  --primary-light: #818CF8;
  --secondary: #06B6D4;
  --tertiary: #A855F7;
  --success: #10B981;
  --warning: #F59E0B;
  --danger: #EF4444;
  --info: #3B82F6;
  --text-primary: #F9FAFB;
  --text-secondary: #9CA3AF;
  --text-muted: #6B7280;
  --border-subtle: rgba(255, 255, 255, 0.08);
  --border-strong: rgba(255, 255, 255, 0.18);
  --glow-primary: 0 0 24px rgba(99, 102, 241, 0.4);
  --glow-cyan: 0 0 20px rgba(6, 182, 212, 0.4);
}

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  width: 1600px;
  height: 1000px;
  background-color: var(--bg-canvas);
  background-image: 
    radial-gradient(circle at 10% 10%, rgba(99, 102, 241, 0.12) 0%, transparent 40%),
    radial-gradient(circle at 90% 90%, rgba(6, 182, 212, 0.08) 0%, transparent 45%),
    linear-gradient(rgba(255, 255, 255, 0.015) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255, 255, 255, 0.015) 1px, transparent 1px);
  background-size: 100% 100%, 100% 100%, 40px 40px, 40px 40px;
  color: var(--text-primary);
  font-family: 'Pretendard', 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  padding: 36px 48px;
  justify-content: space-between;
}

/* Header */
.artboard-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 1px solid var(--border-subtle);
  padding-bottom: 18px;
}

.brand-badge {
  display: flex;
  align-items: center;
  gap: 12px;
}

.brand-logo-icon {
  width: 36px;
  height: 36px;
  border-radius: 8px;
  background: linear-gradient(135deg, #6366F1, #06B6D4);
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 800;
  font-size: 18px;
  color: #FFFFFF;
  box-shadow: 0 0 16px rgba(99, 102, 241, 0.5);
}

.brand-title {
  font-size: 17px;
  font-weight: 700;
  letter-spacing: -0.01em;
  color: #FFFFFF;
}

.brand-sub {
  font-size: 11px;
  color: var(--text-muted);
  font-family: 'JetBrains Mono', monospace;
  letter-spacing: 0.05em;
}

.page-indicator {
  display: flex;
  align-items: center;
  gap: 10px;
  background: var(--bg-surface-1);
  border: 1px solid var(--border-subtle);
  padding: 6px 16px;
  border-radius: 9999px;
}

.page-num {
  font-family: 'JetBrains Mono', monospace;
  font-size: 13px;
  font-weight: 700;
  color: var(--primary-light);
}

.page-category {
  font-size: 12px;
  color: var(--text-secondary);
  font-weight: 600;
  border-left: 1px solid var(--border-subtle);
  padding-left: 10px;
}

/* Content Area */
.artboard-body {
  flex: 1;
  padding: 20px 0;
  display: flex;
  flex-direction: column;
}

.section-header {
  margin-bottom: 18px;
}

.section-tag {
  font-family: 'JetBrains Mono', monospace;
  font-size: 11px;
  font-weight: 700;
  color: var(--secondary);
  text-transform: uppercase;
  letter-spacing: 0.1em;
  margin-bottom: 4px;
}

.section-title {
  font-size: 25px;
  font-weight: 700;
  letter-spacing: -0.02em;
  color: #FFFFFF;
}

.section-desc {
  font-size: 13px;
  color: var(--text-secondary);
  margin-top: 3px;
}

/* Cards & Layout */
.card {
  background: var(--bg-surface-1);
  border: 1px solid var(--border-subtle);
  border-radius: 14px;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4);
  position: relative;
}

.card-elevated {
  background: var(--bg-surface-2);
  border: 1px solid var(--border-strong);
  border-radius: 14px;
  box-shadow: 0 12px 32px rgba(0, 0, 0, 0.5);
}

.card-highlight {
  position: relative;
}
.card-highlight::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 1px;
  background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
}

.grid-2 {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
}

.grid-3 {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  gap: 20px;
}

.grid-4 {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 16px;
}

/* Tables */
.spec-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 12px;
}

.spec-table th {
  background: var(--bg-surface-2);
  color: var(--text-secondary);
  font-weight: 600;
  text-align: left;
  padding: 10px 14px;
  border-bottom: 1px solid var(--border-subtle);
  font-family: 'JetBrains Mono', monospace;
  font-size: 11px;
}

.spec-table td {
  padding: 10px 14px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.04);
  color: var(--text-primary);
}

.spec-table tr:hover td {
  background: rgba(255, 255, 255, 0.02);
}

.code-pill {
  font-family: 'JetBrains Mono', monospace;
  font-size: 11px;
  background: rgba(0, 0, 0, 0.35);
  border: 1px solid var(--border-subtle);
  padding: 2px 6px;
  border-radius: 4px;
  color: var(--primary-light);
}

/* Footer */
.artboard-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-top: 1px solid var(--border-subtle);
  padding-top: 14px;
  font-size: 11px;
  color: var(--text-muted);
  font-family: 'JetBrains Mono', monospace;
}

.footer-system-tag {
  display: flex;
  align-items: center;
  gap: 8px;
}

.footer-dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: var(--success);
  box-shadow: 0 0 8px var(--success);
}
"""

def make_html(page_num, category, title, tag, desc, body_html):
    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <style>
    {COMMON_CSS}
  </style>
</head>
<body>
  <header class="artboard-header">
    <div class="brand-badge">
      <div class="brand-logo-icon">A</div>
      <div>
        <div class="brand-title">NEO-MODERN TECH UI/UX DESIGN SYSTEM</div>
        <div class="brand-sub">AETHER CORE &bull; ENTERPRISE SPECIFICATION v1.0.0</div>
      </div>
    </div>
    <div class="page-indicator">
      <span class="page-num">PAGE {page_num:02d} / 13</span>
      <span class="page-category">{category}</span>
    </div>
  </header>

  <main class="artboard-body">
    <div class="section-header">
      <div class="section-tag">{tag}</div>
      <h1 class="section-title">{title}</h1>
      <div class="section-desc">{desc}</div>
    </div>
    {body_html}
  </main>

  <footer class="artboard-footer">
    <div class="footer-system-tag">
      <span class="footer-dot"></span>
      <span>AETHER CORE DESIGN SYSTEM &bull; STRICT MATHEMATICAL 8-PT GRID</span>
    </div>
    <div>CONFIDENTIAL &bull; BASED ON LOVE.MD ANALYSIS &bull; FOR INTERNAL & PRODUCTION USE</div>
    <div>PAGE {page_num:02d} OF 13</div>
  </footer>
</body>
</html>"""

def get_page_1():
    body = """
    <div style="display: flex; flex-direction: column; gap: 24px; height: 100%; justify-content: space-between;">
      <!-- Hero Box -->
      <div class="card card-highlight" style="padding: 40px 48px; background: linear-gradient(135deg, rgba(17, 24, 39, 0.95), rgba(9, 13, 22, 0.95)); border: 1px solid rgba(99, 102, 241, 0.3); box-shadow: 0 16px 40px rgba(0, 0, 0, 0.6), inset 0 1px 0 rgba(255, 255, 255, 0.1);">
        <div style="display: flex; justify-content: space-between; align-items: flex-start;">
          <div>
            <div style="font-family: 'JetBrains Mono', monospace; font-size: 12px; color: var(--secondary); letter-spacing: 0.15em; font-weight: 700; margin-bottom: 8px;">2026 UI/UX DESIGN SYSTEM SPECIFICATION</div>
            <div style="font-size: 44px; font-weight: 800; letter-spacing: -0.03em; background: linear-gradient(135deg, #FFFFFF 30%, #818CF8 80%, #06B6D4 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; line-height: 1.1; margin-bottom: 12px;">
              AETHER CORE DESIGN SYSTEM
            </div>
            <div style="font-size: 16px; color: var(--text-secondary); max-width: 800px; line-height: 1.5;">
              글로벌 하이엔드 웹/SaaS 레퍼런스 종합 분석 기반 — 딥 슬레이트 옵시디언 캔버스와 사이버 인디고 액센트의 네오 테크 UI/UX 종합 스타일 가이드
            </div>
          </div>
          <div style="background: rgba(99, 102, 241, 0.15); border: 1px solid rgba(99, 102, 241, 0.4); padding: 12px 20px; border-radius: 12px; text-align: right;">
            <div style="font-family: 'JetBrains Mono', monospace; font-size: 11px; color: var(--primary-light);">SYSTEM VERSION</div>
            <div style="font-size: 22px; font-weight: 800; color: #FFFFFF; font-family: 'JetBrains Mono', monospace;">v1.0.0</div>
            <div style="font-size: 11px; color: var(--success);">● PRODUCTION READY</div>
          </div>
        </div>
      </div>

      <!-- 3 Core Pillars -->
      <div class="grid-3">
        <div class="card card-highlight" style="padding: 24px; border-left: 3px solid var(--primary);">
          <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 12px;">
            <div style="width: 28px; height: 28px; border-radius: 6px; background: rgba(99, 102, 241, 0.2); color: var(--primary-light); display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 13px;">01</div>
            <div style="font-size: 17px; font-weight: 700; color: #FFFFFF;">Visual Depth (시각적 뎁스)</div>
          </div>
          <div style="font-size: 13px; color: var(--text-secondary); line-height: 1.6;">
            완전한 블랙 대신 <span class="code-pill">#090D16</span> 캔버스와 3단계 서피스 엘리베이션, 1px 서브틀 보더 및 앰비언트 글로우를 통해 압도적인 깊이감과 가독성을 확보합니다.
          </div>
        </div>

        <div class="card card-highlight" style="padding: 24px; border-left: 3px solid var(--secondary);">
          <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 12px;">
            <div style="width: 28px; height: 28px; border-radius: 6px; background: rgba(6, 182, 212, 0.2); color: var(--secondary); display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 13px;">02</div>
            <div style="font-size: 17px; font-weight: 700; color: #FFFFFF;">Vibrant Clarity (선명한 대비)</div>
          </div>
          <div style="font-size: 13px; color: var(--text-secondary); line-height: 1.6;">
            사이버 인디고(<span class="code-pill">#6366F1</span>)와 네온 시안(<span class="code-pill">#06B6D4</span>)을 핵심 액센트로 배치하여 0.3초 내 주요 CTA와 상태 변화를 명확히 인지시킵니다.
          </div>
        </div>

        <div class="card card-highlight" style="padding: 24px; border-left: 3px solid var(--tertiary);">
          <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 12px;">
            <div style="width: 28px; height: 28px; border-radius: 6px; background: rgba(168, 85, 247, 0.2); color: var(--tertiary); display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 13px;">03</div>
            <div style="font-size: 17px; font-weight: 700; color: #FFFFFF;">Precision Geometry (정밀한 기하학)</div>
          </div>
          <div style="font-size: 13px; color: var(--text-secondary); line-height: 1.6;">
            8pt 엄격한 수학적 그리드와 12px/16px 유려한 라운딩, 마이크로 인터랙션 피드백을 적용하여 디자인과 프론트엔드 구현 간 오차 0%를 달성합니다.
          </div>
        </div>
      </div>

      <!-- Metadata Bar -->
      <div class="card" style="padding: 18px 24px; display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px; background: var(--bg-surface-1);">
        <div>
          <div style="font-family: 'JetBrains Mono', monospace; font-size: 11px; color: var(--text-muted);">AUTHOR / ROLE</div>
          <div style="font-size: 13px; font-weight: 600; color: var(--text-primary); margin-top: 2px;">수석 UI/UX 디자이너 & 엔지니어</div>
        </div>
        <div>
          <div style="font-family: 'JetBrains Mono', monospace; font-size: 11px; color: var(--text-muted);">RESOLUTION BASELINE</div>
          <div style="font-size: 13px; font-weight: 600; color: var(--text-primary); margin-top: 2px;">Desktop 1440px / Mobile 390px</div>
        </div>
        <div>
          <div style="font-family: 'JetBrains Mono', monospace; font-size: 11px; color: var(--text-muted);">COLOR PROFILE</div>
          <div style="font-size: 13px; font-weight: 600; color: var(--text-primary); margin-top: 2px;">sRGB / Display P3 Ready</div>
        </div>
        <div>
          <div style="font-family: 'JetBrains Mono', monospace; font-size: 11px; color: var(--text-muted);">TARGET PRODUCTS</div>
          <div style="font-size: 13px; font-weight: 600; color: var(--text-primary); margin-top: 2px;">AI SaaS &bull; B2B &bull; Quiz Platform</div>
        </div>
      </div>
    </div>
    """
    return make_html(1, "OVERVIEW", "Cover (스타일 가이드 메인 타이틀 및 컨셉 요약)", "Design System Cover", "Aether Core — 하이엔드 네오 테크 & 정제된 미니멀리즘 디자인 시스템 총괄 명세", body)

def get_page_2():
    body = """
    <div style="display: flex; flex-direction: column; gap: 20px;">
      <div class="grid-2">
        <!-- Principles -->
        <div class="card" style="padding: 24px; display: flex; flex-direction: column; gap: 16px;">
          <div style="font-size: 16px; font-weight: 700; color: #FFFFFF; border-bottom: 1px solid var(--border-subtle); padding-bottom: 10px; display: flex; align-items: center; gap: 8px;">
            <span style="color: var(--primary-light);">●</span> 디자인 4대 핵심 원칙 (Core Principles)
          </div>
          
          <div style="display: flex; gap: 12px;">
            <div style="width: 24px; height: 24px; border-radius: 6px; background: rgba(99,102,241,0.2); color: var(--primary-light); display: flex; align-items: center; justify-content: center; font-size: 12px; font-weight: 700; flex-shrink: 0;">1</div>
            <div>
              <div style="font-size: 14px; font-weight: 700; color: var(--text-primary);">Hierarchy First (명확한 정보 위계)</div>
              <div style="font-size: 12px; color: var(--text-secondary); margin-top: 2px; line-height: 1.5;">타이포 크기, 자간, 투명도를 통해 0.3초 내 핵심 액션을 직관적으로 인지하도록 설계.</div>
            </div>
          </div>

          <div style="display: flex; gap: 12px;">
            <div style="width: 24px; height: 24px; border-radius: 6px; background: rgba(99,102,241,0.2); color: var(--primary-light); display: flex; align-items: center; justify-content: center; font-size: 12px; font-weight: 700; flex-shrink: 0;">2</div>
            <div>
              <div style="font-size: 14px; font-weight: 700; color: var(--text-primary);">Deep Immersive Canvas (몰입형 딥 다크)</div>
              <div style="font-size: 12px; color: var(--text-secondary); margin-top: 2px; line-height: 1.5;">눈의 피로를 최소화하는 <span class="code-pill">#090D16</span> 베이스와 3단계 카드 계층으로 자연스러운 3D 뎁스 형성.</div>
            </div>
          </div>

          <div style="display: flex; gap: 12px;">
            <div style="width: 24px; height: 24px; border-radius: 6px; background: rgba(99,102,241,0.2); color: var(--primary-light); display: flex; align-items: center; justify-content: center; font-size: 12px; font-weight: 700; flex-shrink: 0;">3</div>
            <div>
              <div style="font-size: 14px; font-weight: 700; color: var(--text-primary);">Tactile & Responsive (물리적 피드백)</div>
              <div style="font-size: 12px; color: var(--text-secondary); margin-top: 2px; line-height: 1.5;">호버/클릭 시 단순 색상 변경을 넘어 1px 하이라이트와 앰비언트 글로우로 직관적 물리감 제공.</div>
            </div>
          </div>

          <div style="display: flex; gap: 12px;">
            <div style="width: 24px; height: 24px; border-radius: 6px; background: rgba(99,102,241,0.2); color: var(--primary-light); display: flex; align-items: center; justify-content: center; font-size: 12px; font-weight: 700; flex-shrink: 0;">4</div>
            <div>
              <div style="font-size: 14px; font-weight: 700; color: var(--text-primary);">Strict Modularity (엄격한 모듈화)</div>
              <div style="font-size: 12px; color: var(--text-secondary); margin-top: 2px; line-height: 1.5;">모든 컴포넌트는 독립적이며 4px/8px 단위로 오차 없이 완벽하게 결합 및 확장.</div>
            </div>
          </div>
        </div>

        <!-- Token Rules -->
        <div class="card" style="padding: 24px; display: flex; flex-direction: column; gap: 16px;">
          <div style="font-size: 16px; font-weight: 700; color: #FFFFFF; border-bottom: 1px solid var(--border-subtle); padding-bottom: 10px; display: flex; align-items: center; gap: 8px;">
            <span style="color: var(--secondary);">●</span> 디자인 토큰 및 코드 적용 규칙
          </div>

          <div style="background: var(--bg-surface-2); padding: 14px; border-radius: 10px; border: 1px solid var(--border-subtle);">
            <div style="font-size: 13px; font-weight: 700; color: var(--secondary); margin-bottom: 4px;">1. Hardcoded Value 금지</div>
            <div style="font-size: 12px; color: var(--text-secondary); line-height: 1.5;">
              임의의 <span class="code-pill">px</span> 또는 <span class="code-pill">#HEX</span> 직접 지정을 금지하며, 반드시 정의된 CSS Variable 토큰을 사용합니다.
            </div>
          </div>

          <div style="background: var(--bg-surface-2); padding: 14px; border-radius: 10px; border: 1px solid var(--border-subtle);">
            <div style="font-size: 13px; font-weight: 700; color: var(--primary-light); margin-bottom: 4px;">2. 반투명 보더(Alpha Border) 원칙</div>
            <div style="font-size: 12px; color: var(--text-secondary); line-height: 1.5;">
              보더는 불투명 단색 대신 <span class="code-pill">rgba(255, 255, 255, 0.08)</span>를 적용하여 다크 배경 계층 변화에 적응형으로 반응합니다.
            </div>
          </div>

          <div style="background: var(--bg-surface-2); padding: 14px; border-radius: 10px; border: 1px solid var(--border-subtle);">
            <div style="font-size: 13px; font-weight: 700; color: var(--success); margin-bottom: 4px;">3. 상태 피드백 3단계 일관성</div>
            <div style="font-size: 12px; color: var(--text-secondary); line-height: 1.5;">
              모든 인터랙티브 컴포넌트는 <span class="code-pill">Default</span> &rarr; <span class="code-pill">Hover (+Glow)</span> &rarr; <span class="code-pill">Active/Pressed</span>의 표준 3단계 상태를 가집니다.
            </div>
          </div>
        </div>
      </div>

      <!-- Quick Token Mapping -->
      <div class="card" style="padding: 18px 24px;">
        <div style="font-size: 14px; font-weight: 700; color: #FFFFFF; margin-bottom: 12px; font-family: 'JetBrains Mono', monospace;">QUICK SYSTEM TOKEN MAPPING</div>
        <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 14px; font-size: 12px;">
          <div style="background: rgba(0,0,0,0.3); padding: 10px 14px; border-radius: 8px; border: 1px solid var(--border-subtle);">
            <div style="color: var(--text-muted); font-size: 11px;">Primary Action</div>
            <div style="color: var(--primary-light); font-weight: 700; font-family: 'JetBrains Mono', monospace;">var(--primary) : #6366F1</div>
          </div>
          <div style="background: rgba(0,0,0,0.3); padding: 10px 14px; border-radius: 8px; border: 1px solid var(--border-subtle);">
            <div style="color: var(--text-muted); font-size: 11px;">Canvas Background</div>
            <div style="color: var(--text-primary); font-weight: 700; font-family: 'JetBrains Mono', monospace;">var(--bg-canvas) : #090D16</div>
          </div>
          <div style="background: rgba(0,0,0,0.3); padding: 10px 14px; border-radius: 8px; border: 1px solid var(--border-subtle);">
            <div style="color: var(--text-muted); font-size: 11px;">Card Surface</div>
            <div style="color: var(--text-primary); font-weight: 700; font-family: 'JetBrains Mono', monospace;">var(--bg-surface-1) : #111827</div>
          </div>
          <div style="background: rgba(0,0,0,0.3); padding: 10px 14px; border-radius: 8px; border: 1px solid var(--border-subtle);">
            <div style="color: var(--text-muted); font-size: 11px;">Base Spacing Unit</div>
            <div style="color: var(--secondary); font-weight: 700; font-family: 'JetBrains Mono', monospace;">8px Grid / 4px Sub-grid</div>
          </div>
        </div>
      </div>
    </div>
    """
    return make_html(2, "FOUNDATIONS", "Getting Started (디자인 원칙 및 시작 가이드)", "Design Principles & Token Rules", "Aether Core 디자인 시스템의 설계 원칙 및 토큰 활용 가이드라인", body)

def get_page_3():
    body = """
    <div style="display: flex; flex-direction: column; gap: 16px;">
      <div class="grid-2" style="gap: 16px;">
        <!-- Brand Primary & Accent -->
        <div class="card" style="padding: 20px;">
          <div style="font-size: 14px; font-weight: 700; color: #FFFFFF; margin-bottom: 12px; display: flex; justify-content: space-between;">
            <span>Brand Primary & Accent</span>
            <span style="font-family: 'JetBrains Mono', monospace; font-size: 11px; color: var(--secondary);">CORE PALETTE</span>
          </div>
          <div style="display: flex; flex-direction: column; gap: 8px;">
            <div style="display: flex; align-items: center; justify-content: space-between; background: var(--bg-surface-2); padding: 8px 12px; border-radius: 8px;">
              <div style="display: flex; align-items: center; gap: 10px;">
                <div style="width: 28px; height: 28px; border-radius: 6px; background: #6366F1; box-shadow: 0 0 10px rgba(99,102,241,0.5);"></div>
                <div>
                  <div style="font-size: 13px; font-weight: 700; color: #FFF;">Primary Main (Indigo)</div>
                  <div style="font-size: 11px; color: var(--text-muted);">주요 CTA, 활성 상태, 포커스 링</div>
                </div>
              </div>
              <div style="text-align: right; font-family: 'JetBrains Mono', monospace;">
                <div style="color: var(--primary-light); font-weight: 700; font-size: 12px;">#6366F1</div>
                <div style="color: var(--text-muted); font-size: 10px;">RGB(99, 102, 241)</div>
              </div>
            </div>

            <div style="display: flex; align-items: center; justify-content: space-between; background: var(--bg-surface-2); padding: 8px 12px; border-radius: 8px;">
              <div style="display: flex; align-items: center; gap: 10px;">
                <div style="width: 28px; height: 28px; border-radius: 6px; background: #4F46E5;"></div>
                <div>
                  <div style="font-size: 13px; font-weight: 700; color: #FFF;">Primary Hover</div>
                  <div style="font-size: 11px; color: var(--text-muted);">버튼 및 링크 호버 시 상태</div>
                </div>
              </div>
              <div style="text-align: right; font-family: 'JetBrains Mono', monospace;">
                <div style="color: var(--primary-light); font-weight: 700; font-size: 12px;">#4F46E5</div>
                <div style="color: var(--text-muted); font-size: 10px;">RGB(79, 70, 229)</div>
              </div>
            </div>

            <div style="display: flex; align-items: center; justify-content: space-between; background: var(--bg-surface-2); padding: 8px 12px; border-radius: 8px;">
              <div style="display: flex; align-items: center; gap: 10px;">
                <div style="width: 28px; height: 28px; border-radius: 6px; background: #06B6D4; box-shadow: 0 0 10px rgba(6,182,212,0.5);"></div>
                <div>
                  <div style="font-size: 13px; font-weight: 700; color: #FFF;">Secondary (Neon Cyan)</div>
                  <div style="font-size: 11px; color: var(--text-muted);">프로그레스, 타이머, 데이터 차트</div>
                </div>
              </div>
              <div style="text-align: right; font-family: 'JetBrains Mono', monospace;">
                <div style="color: var(--secondary); font-weight: 700; font-size: 12px;">#06B6D4</div>
                <div style="color: var(--text-muted); font-size: 10px;">RGB(6, 182, 212)</div>
              </div>
            </div>

            <div style="display: flex; align-items: center; justify-content: space-between; background: var(--bg-surface-2); padding: 8px 12px; border-radius: 8px;">
              <div style="display: flex; align-items: center; gap: 10px;">
                <div style="width: 28px; height: 28px; border-radius: 6px; background: #A855F7; box-shadow: 0 0 10px rgba(168,85,247,0.5);"></div>
                <div>
                  <div style="font-size: 13px; font-weight: 700; color: #FFF;">Tertiary (Electric Violet)</div>
                  <div style="font-size: 11px; color: var(--text-muted);">AI 추천, 스페셜 뱃지</div>
                </div>
              </div>
              <div style="text-align: right; font-family: 'JetBrains Mono', monospace;">
                <div style="color: var(--tertiary); font-weight: 700; font-size: 12px;">#A855F7</div>
                <div style="color: var(--text-muted); font-size: 10px;">RGB(168, 85, 247)</div>
              </div>
            </div>
          </div>
        </div>

        <!-- Dark Neutral Surfaces -->
        <div class="card" style="padding: 20px;">
          <div style="font-size: 14px; font-weight: 700; color: #FFFFFF; margin-bottom: 12px; display: flex; justify-content: space-between;">
            <span>Dark Neutral Surfaces & Borders</span>
            <span style="font-family: 'JetBrains Mono', monospace; font-size: 11px; color: var(--secondary);">SURFACE ELEVATION</span>
          </div>
          <div style="display: flex; flex-direction: column; gap: 8px;">
            <div style="display: flex; align-items: center; justify-content: space-between; background: var(--bg-surface-2); padding: 8px 12px; border-radius: 8px;">
              <div style="display: flex; align-items: center; gap: 10px;">
                <div style="width: 28px; height: 28px; border-radius: 6px; background: #090D16; border: 1px solid rgba(255,255,255,0.2);"></div>
                <div>
                  <div style="font-size: 13px; font-weight: 700; color: #FFF;">Canvas Base (Deep Background)</div>
                  <div style="font-size: 11px; color: var(--text-muted);">최하단 배경 캔버스</div>
                </div>
              </div>
              <div style="text-align: right; font-family: 'JetBrains Mono', monospace;">
                <div style="color: var(--text-primary); font-weight: 700; font-size: 12px;">#090D16</div>
                <div style="color: var(--text-muted); font-size: 10px;">RGB(9, 13, 22)</div>
              </div>
            </div>

            <div style="display: flex; align-items: center; justify-content: space-between; background: var(--bg-surface-2); padding: 8px 12px; border-radius: 8px;">
              <div style="display: flex; align-items: center; gap: 10px;">
                <div style="width: 28px; height: 28px; border-radius: 6px; background: #111827; border: 1px solid rgba(255,255,255,0.2);"></div>
                <div>
                  <div style="font-size: 13px; font-weight: 700; color: #FFF;">Surface Level 1 (Card / Container)</div>
                  <div style="font-size: 11px; color: var(--text-muted);">기본 카드, 컨테이너 영역</div>
                </div>
              </div>
              <div style="text-align: right; font-family: 'JetBrains Mono', monospace;">
                <div style="color: var(--text-primary); font-weight: 700; font-size: 12px;">#111827</div>
                <div style="color: var(--text-muted); font-size: 10px;">RGB(17, 24, 39)</div>
              </div>
            </div>

            <div style="display: flex; align-items: center; justify-content: space-between; background: var(--bg-surface-2); padding: 8px 12px; border-radius: 8px;">
              <div style="display: flex; align-items: center; gap: 10px;">
                <div style="width: 28px; height: 28px; border-radius: 6px; background: #1F2937; border: 1px solid rgba(255,255,255,0.2);"></div>
                <div>
                  <div style="font-size: 13px; font-weight: 700; color: #FFF;">Surface Level 2 (Elevated / Modal)</div>
                  <div style="font-size: 11px; color: var(--text-muted);">모달, 드롭다운, 강조 패널</div>
                </div>
              </div>
              <div style="text-align: right; font-family: 'JetBrains Mono', monospace;">
                <div style="color: var(--text-primary); font-weight: 700; font-size: 12px;">#1F2937</div>
                <div style="color: var(--text-muted); font-size: 10px;">RGB(31, 41, 55)</div>
              </div>
            </div>

            <div style="display: flex; align-items: center; justify-content: space-between; background: var(--bg-surface-2); padding: 8px 12px; border-radius: 8px;">
              <div style="display: flex; align-items: center; gap: 10px;">
                <div style="width: 28px; height: 28px; border-radius: 6px; background: rgba(255,255,255,0.08); border: 1px solid rgba(255,255,255,0.3);"></div>
                <div>
                  <div style="font-size: 13px; font-weight: 700; color: #FFF;">Border Subtle & Strong</div>
                  <div style="font-size: 11px; color: var(--text-muted);">1px 반투명 계층 구분선</div>
                </div>
              </div>
              <div style="text-align: right; font-family: 'JetBrains Mono', monospace;">
                <div style="color: var(--text-secondary); font-weight: 700; font-size: 12px;">rgba(255,255,255,0.08)</div>
                <div style="color: var(--text-muted); font-size: 10px;">Strong: 0.18</div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Semantic Status Colors -->
      <div class="card" style="padding: 16px 20px;">
        <div style="font-size: 13px; font-weight: 700; color: #FFFFFF; margin-bottom: 10px;">Semantic Status Colors (상태 피드백 색상)</div>
        <div class="grid-4" style="gap: 12px;">
          <div style="background: rgba(16, 185, 129, 0.12); border: 1px solid rgba(16, 185, 129, 0.35); padding: 10px 14px; border-radius: 8px;">
            <div style="display: flex; align-items: center; gap: 6px; color: #10B981; font-weight: 700; font-size: 13px;">
              <span>●</span> Success (정답/완료)
            </div>
            <div style="font-family: 'JetBrains Mono', monospace; font-size: 11px; color: #A7F3D0; margin-top: 4px;">#10B981 &bull; 10% BG</div>
          </div>

          <div style="background: rgba(245, 158, 11, 0.12); border: 1px solid rgba(245, 158, 11, 0.35); padding: 10px 14px; border-radius: 8px;">
            <div style="display: flex; align-items: center; gap: 6px; color: #F59E0B; font-weight: 700; font-size: 13px;">
              <span>●</span> Warning (주의/임박)
            </div>
            <div style="font-family: 'JetBrains Mono', monospace; font-size: 11px; color: #FDE68A; margin-top: 4px;">#F59E0B &bull; 10% BG</div>
          </div>

          <div style="background: rgba(239, 68, 68, 0.12); border: 1px solid rgba(239, 68, 68, 0.35); padding: 10px 14px; border-radius: 8px;">
            <div style="display: flex; align-items: center; gap: 6px; color: #EF4444; font-weight: 700; font-size: 13px;">
              <span>●</span> Danger (오답/만료)
            </div>
            <div style="font-family: 'JetBrains Mono', monospace; font-size: 11px; color: #FECACA; margin-top: 4px;">#EF4444 &bull; 10% BG</div>
          </div>

          <div style="background: rgba(59, 130, 246, 0.12); border: 1px solid rgba(59, 130, 246, 0.35); padding: 10px 14px; border-radius: 8px;">
            <div style="display: flex; align-items: center; gap: 6px; color: #3B82F6; font-weight: 700; font-size: 13px;">
              <span>●</span> Info (안내/힌트)
            </div>
            <div style="font-family: 'JetBrains Mono', monospace; font-size: 11px; color: #BFDBFE; margin-top: 4px;">#3B82F6 &bull; 10% BG</div>
          </div>
        </div>
      </div>
    </div>
    """
    return make_html(3, "FOUNDATIONS", "Colors (색상 체계 & Hex 코드)", "Color System & Tokens", "Aether Core 브랜드 프라이머리, 서피스 계층, 시맨틱 상태 컬러 전체 스펙", body)

def get_page_4():
    body = """
    <div style="display: flex; flex-direction: column; gap: 16px;">
      <!-- Font Families -->
      <div class="grid-2" style="gap: 16px;">
        <div class="card" style="padding: 16px 20px;">
          <div style="font-family: 'JetBrains Mono', monospace; font-size: 11px; color: var(--secondary);">PRIMARY UI FONT</div>
          <div style="font-size: 18px; font-weight: 700; color: #FFF; margin-top: 2px;">Pretendard / Inter</div>
          <div style="font-size: 12px; color: var(--text-secondary); margin-top: 4px;">
            가독성과 렌더링 완성도가 뛰어난 산세리프 폰트. 국문/영문 UI 텍스트 및 본문 전반 적용.
          </div>
        </div>
        <div class="card" style="padding: 16px 20px;">
          <div style="font-family: 'JetBrains Mono', monospace; font-size: 11px; color: var(--primary-light);">NUMBERS & CODE FONT</div>
          <div style="font-size: 18px; font-weight: 700; color: #FFF; margin-top: 2px; font-family: 'JetBrains Mono', monospace;">JetBrains Mono / Geist Mono</div>
          <div style="font-size: 12px; color: var(--text-secondary); margin-top: 4px;">
            고정폭(Monospace) 폰트로 타이머, 점수, 통계 수치 및 코드 스니펫에 정밀한 정렬감 부여.
          </div>
        </div>
      </div>

      <!-- Typography Scale Table -->
      <div class="card" style="padding: 16px 20px; overflow: hidden;">
        <div style="font-size: 14px; font-weight: 700; color: #FFF; margin-bottom: 10px;">Typography Scale Specification</div>
        <table class="spec-table">
          <thead>
            <tr>
              <th>TOKEN</th>
              <th>FONT SIZE</th>
              <th>LINE HEIGHT</th>
              <th>WEIGHT</th>
              <th>TRACKING</th>
              <th>USAGE</th>
              <th>VISUAL SAMPLE</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><span class="code-pill">Display 1</span></td>
              <td>40px (2.5rem)</td>
              <td>48px (1.2)</td>
              <td>Bold (700)</td>
              <td>-0.02em</td>
              <td>히어로 메인 타이틀, 스코어</td>
              <td><span style="font-size: 20px; font-weight: 700; color: #FFF;">Aether Core</span></td>
            </tr>
            <tr>
              <td><span class="code-pill">Heading 1</span></td>
              <td>32px (2.0rem)</td>
              <td>40px (1.25)</td>
              <td>Bold (700)</td>
              <td>-0.015em</td>
              <td>메인 섹션 헤더, 퀴즈 대제목</td>
              <td><span style="font-size: 18px; font-weight: 700; color: #FFF;">Design System</span></td>
            </tr>
            <tr>
              <td><span class="code-pill">Heading 2</span></td>
              <td>24px (1.5rem)</td>
              <td>32px (1.33)</td>
              <td>SemiBold (600)</td>
              <td>-0.01em</td>
              <td>카드 타이틀, 질문 문항 헤더</td>
              <td><span style="font-size: 16px; font-weight: 600; color: #FFF;">Question Title</span></td>
            </tr>
            <tr>
              <td><span class="code-pill">Heading 3</span></td>
              <td>20px (1.25rem)</td>
              <td>28px (1.4)</td>
              <td>SemiBold (600)</td>
              <td>0.0em</td>
              <td>모달 헤더, 서브 컴포넌트 타이틀</td>
              <td><span style="font-size: 15px; font-weight: 600; color: #FFF;">Modal Dialog</span></td>
            </tr>
            <tr>
              <td><span class="code-pill">Body Large</span></td>
              <td>16px (1.0rem)</td>
              <td>24px (1.5)</td>
              <td>Medium (500)</td>
              <td>0.0em</td>
              <td>퀴즈 문항 본문, 선택지 텍스트</td>
              <td><span style="font-size: 14px; font-weight: 500; color: var(--text-primary);">Standard Question Body</span></td>
            </tr>
            <tr>
              <td><span class="code-pill">Body Regular</span></td>
              <td>14px (0.875rem)</td>
              <td>20px (1.43)</td>
              <td>Regular (400)</td>
              <td>+0.01em</td>
              <td>기본 본문, 일반 설명 텍스트</td>
              <td><span style="font-size: 13px; color: var(--text-secondary);">Default UI text description</span></td>
            </tr>
            <tr>
              <td><span class="code-pill">Caption</span></td>
              <td>12px (0.75rem)</td>
              <td>16px (1.33)</td>
              <td>Medium (500)</td>
              <td>+0.02em</td>
              <td>상태 뱃지, 타임스탬프, 캡션</td>
              <td><span style="font-size: 12px; color: var(--text-muted);">Badge & Timestamp</span></td>
            </tr>
            <tr>
              <td><span class="code-pill">Micro</span></td>
              <td>10px (0.625rem)</td>
              <td>14px (1.4)</td>
              <td>SemiBold (600)</td>
              <td>+0.04em</td>
              <td>카테고리 태그, 인디케이터 라벨</td>
              <td><span style="font-size: 10px; font-weight: 600; color: var(--secondary); text-transform: uppercase;">CATEGORY TAG</span></td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    """
    return make_html(4, "FOUNDATIONS", "Typography (타이포그래피 시스템)", "Type Scale & Font Family", "폰트 패밀리 구성, 헤딩/본문/캡션 크기 및 행간(Line-height) 상세 스펙", body)

def get_page_5():
    body = """
    <div style="display: flex; flex-direction: column; gap: 16px;">
      <!-- Spacing Tokens -->
      <div class="card" style="padding: 20px;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
          <div style="font-size: 14px; font-weight: 700; color: #FFF;">8-Point Mathematical Spacing Scale</div>
          <div style="font-family: 'JetBrains Mono', monospace; font-size: 11px; color: var(--secondary);">BASE UNIT: 8PX (SUB: 4PX)</div>
        </div>
        <div class="grid-4" style="gap: 12px;">
          <div style="background: var(--bg-surface-2); padding: 10px 14px; border-radius: 8px; border: 1px solid var(--border-subtle);">
            <div style="display: flex; justify-content: space-between;">
              <span class="code-pill">space-4</span>
              <span style="font-family: 'JetBrains Mono', monospace; color: var(--primary-light); font-size: 12px; font-weight: 700;">4px</span>
            </div>
            <div style="height: 4px; width: 100%; background: var(--primary); margin: 8px 0; border-radius: 2px;"></div>
            <div style="font-size: 11px; color: var(--text-muted);">아이콘-텍스트 간격, 뱃지 내부</div>
          </div>

          <div style="background: var(--bg-surface-2); padding: 10px 14px; border-radius: 8px; border: 1px solid var(--border-subtle);">
            <div style="display: flex; justify-content: space-between;">
              <span class="code-pill">space-8</span>
              <span style="font-family: 'JetBrains Mono', monospace; color: var(--primary-light); font-size: 12px; font-weight: 700;">8px</span>
            </div>
            <div style="height: 8px; width: 100%; background: var(--primary); margin: 8px 0; border-radius: 2px;"></div>
            <div style="font-size: 11px; color: var(--text-muted);">콤팩트 요소 간격, 태그 갭</div>
          </div>

          <div style="background: var(--bg-surface-2); padding: 10px 14px; border-radius: 8px; border: 1px solid var(--border-subtle);">
            <div style="display: flex; justify-content: space-between;">
              <span class="code-pill">space-12</span>
              <span style="font-family: 'JetBrains Mono', monospace; color: var(--primary-light); font-size: 12px; font-weight: 700;">12px</span>
            </div>
            <div style="height: 12px; width: 100%; background: var(--primary); margin: 8px 0; border-radius: 2px;"></div>
            <div style="font-size: 11px; color: var(--text-muted);">버튼 패딩, 인풋 내부 여백</div>
          </div>

          <div style="background: var(--bg-surface-2); padding: 10px 14px; border-radius: 8px; border: 1px solid var(--border-subtle);">
            <div style="display: flex; justify-content: space-between;">
              <span class="code-pill">space-16</span>
              <span style="font-family: 'JetBrains Mono', monospace; color: var(--primary-light); font-size: 12px; font-weight: 700;">16px</span>
            </div>
            <div style="height: 16px; width: 100%; background: var(--primary); margin: 8px 0; border-radius: 2px;"></div>
            <div style="font-size: 11px; color: var(--text-muted);">표준 컴포넌트 내부 패딩</div>
          </div>

          <div style="background: var(--bg-surface-2); padding: 10px 14px; border-radius: 8px; border: 1px solid var(--border-subtle);">
            <div style="display: flex; justify-content: space-between;">
              <span class="code-pill">space-20</span>
              <span style="font-family: 'JetBrains Mono', monospace; color: var(--primary-light); font-size: 12px; font-weight: 700;">20px</span>
            </div>
            <div style="height: 20px; width: 100%; background: var(--secondary); margin: 8px 0; border-radius: 2px;"></div>
            <div style="font-size: 11px; color: var(--text-muted);">카드 기본 내부 패딩</div>
          </div>

          <div style="background: var(--bg-surface-2); padding: 10px 14px; border-radius: 8px; border: 1px solid var(--border-subtle);">
            <div style="display: flex; justify-content: space-between;">
              <span class="code-pill">space-24</span>
              <span style="font-family: 'JetBrains Mono', monospace; color: var(--primary-light); font-size: 12px; font-weight: 700;">24px</span>
            </div>
            <div style="height: 24px; width: 100%; background: var(--secondary); margin: 8px 0; border-radius: 2px;"></div>
            <div style="font-size: 11px; color: var(--text-muted);">대형 카드 패딩, 요소 간격</div>
          </div>

          <div style="background: var(--bg-surface-2); padding: 10px 14px; border-radius: 8px; border: 1px solid var(--border-subtle);">
            <div style="display: flex; justify-content: space-between;">
              <span class="code-pill">space-32</span>
              <span style="font-family: 'JetBrains Mono', monospace; color: var(--primary-light); font-size: 12px; font-weight: 700;">32px</span>
            </div>
            <div style="height: 32px; width: 100%; background: var(--tertiary); margin: 8px 0; border-radius: 2px;"></div>
            <div style="font-size: 11px; color: var(--text-muted);">섹션 간 마진 및 거더 여백</div>
          </div>

          <div style="background: var(--bg-surface-2); padding: 10px 14px; border-radius: 8px; border: 1px solid var(--border-subtle);">
            <div style="display: flex; justify-content: space-between;">
              <span class="code-pill">space-48</span>
              <span style="font-family: 'JetBrains Mono', monospace; color: var(--primary-light); font-size: 12px; font-weight: 700;">48px</span>
            </div>
            <div style="height: 48px; width: 100%; background: var(--tertiary); margin: 8px 0; border-radius: 2px;"></div>
            <div style="font-size: 11px; color: var(--text-muted);">메인 레이아웃 블록 간격</div>
          </div>
        </div>
      </div>

      <!-- Responsive Grid Layout -->
      <div class="card" style="padding: 20px;">
        <div style="font-size: 14px; font-weight: 700; color: #FFF; margin-bottom: 12px;">Responsive Grid Layout Specifications</div>
        <div class="grid-3" style="gap: 16px;">
          <div style="background: var(--bg-surface-2); padding: 14px; border-radius: 10px; border-top: 3px solid var(--primary);">
            <div style="display: flex; justify-content: space-between; align-items: center;">
              <span style="font-weight: 700; font-size: 14px; color: #FFF;">Desktop</span>
              <span class="code-pill">12 Columns</span>
            </div>
            <div style="margin-top: 8px; font-size: 12px; color: var(--text-secondary); line-height: 1.6;">
              &bull; Max Width: <strong style="color:#FFF;">1280px</strong><br>
              &bull; Gutter: <strong style="color:#FFF;">24px</strong><br>
              &bull; Margin: <strong style="color:#FFF;">32px</strong>
            </div>
          </div>

          <div style="background: var(--bg-surface-2); padding: 14px; border-radius: 10px; border-top: 3px solid var(--secondary);">
            <div style="display: flex; justify-content: space-between; align-items: center;">
              <span style="font-weight: 700; font-size: 14px; color: #FFF;">Tablet</span>
              <span class="code-pill">8 Columns</span>
            </div>
            <div style="margin-top: 8px; font-size: 12px; color: var(--text-secondary); line-height: 1.6;">
              &bull; Max Width: <strong style="color:#FFF;">768px</strong><br>
              &bull; Gutter: <strong style="color:#FFF;">16px</strong><br>
              &bull; Margin: <strong style="color:#FFF;">24px</strong>
            </div>
          </div>

          <div style="background: var(--bg-surface-2); padding: 14px; border-radius: 10px; border-top: 3px solid var(--tertiary);">
            <div style="display: flex; justify-content: space-between; align-items: center;">
              <span style="font-weight: 700; font-size: 14px; color: #FFF;">Mobile</span>
              <span class="code-pill">4 Columns</span>
            </div>
            <div style="margin-top: 8px; font-size: 12px; color: var(--text-secondary); line-height: 1.6;">
              &bull; Max Width: <strong style="color:#FFF;">390px</strong><br>
              &bull; Gutter: <strong style="color:#FFF;">12px</strong><br>
              &bull; Margin: <strong style="color:#FFF;">16px</strong>
            </div>
          </div>
        </div>
      </div>
    </div>
    """
    return make_html(5, "FOUNDATIONS", "Spacing & Sizing (스페이싱 & 그리드 시스템)", "Layout Grid & Spacing Tokens", "8-Point 수학적 스페이싱 토큰 및 반응형 12-Column 그리드 레이아웃 명세", body)

def get_page_6():
    body = """
    <div style="display: flex; flex-direction: column; gap: 16px;">
      <!-- Corner Radius Scale -->
      <div class="card" style="padding: 20px;">
        <div style="font-size: 14px; font-weight: 700; color: #FFF; margin-bottom: 12px; display: flex; justify-content: space-between;">
          <span>Corner Radius Tokens</span>
          <span style="font-family: 'JetBrains Mono', monospace; font-size: 11px; color: var(--secondary);">RADIUS SYSTEM</span>
        </div>
        <div class="grid-3" style="gap: 14px;">
          <div style="background: var(--bg-surface-2); padding: 14px; border-radius: 8px; display: flex; align-items: center; gap: 14px;">
            <div style="width: 50px; height: 50px; background: rgba(99,102,241,0.2); border: 1.5px solid var(--primary); border-radius: 4px; display: flex; align-items: center; justify-content: center; font-size: 11px; font-family: 'JetBrains Mono', monospace; color: var(--primary-light);">4px</div>
            <div>
              <div style="font-size: 13px; font-weight: 700; color: #FFF;"><span class="code-pill">r-xs (4px)</span></div>
              <div style="font-size: 11px; color: var(--text-muted); margin-top: 2px;">툴팁, 미니 태그, 코드 블록</div>
            </div>
          </div>

          <div style="background: var(--bg-surface-2); padding: 14px; border-radius: 8px; display: flex; align-items: center; gap: 14px;">
            <div style="width: 50px; height: 50px; background: rgba(99,102,241,0.2); border: 1.5px solid var(--primary); border-radius: 8px; display: flex; align-items: center; justify-content: center; font-size: 11px; font-family: 'JetBrains Mono', monospace; color: var(--primary-light);">8px</div>
            <div>
              <div style="font-size: 13px; font-weight: 700; color: #FFF;"><span class="code-pill">r-sm (8px)</span></div>
              <div style="font-size: 11px; color: var(--text-muted); margin-top: 2px;">상태 뱃지, 서브 입력 필드</div>
            </div>
          </div>

          <div style="background: var(--bg-surface-2); padding: 14px; border-radius: 8px; display: flex; align-items: center; gap: 14px;">
            <div style="width: 50px; height: 50px; background: rgba(99,102,241,0.2); border: 1.5px solid var(--primary); border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 11px; font-family: 'JetBrains Mono', monospace; color: var(--primary-light);">12px</div>
            <div>
              <div style="font-size: 13px; font-weight: 700; color: #FFF;"><span class="code-pill">r-md (12px)</span></div>
              <div style="font-size: 11px; color: var(--text-muted); margin-top: 2px;">일반 버튼, 퀴즈 선택지 카드</div>
            </div>
          </div>

          <div style="background: var(--bg-surface-2); padding: 14px; border-radius: 8px; display: flex; align-items: center; gap: 14px;">
            <div style="width: 50px; height: 50px; background: rgba(6,182,212,0.2); border: 1.5px solid var(--secondary); border-radius: 16px; display: flex; align-items: center; justify-content: center; font-size: 11px; font-family: 'JetBrains Mono', monospace; color: var(--secondary);">16px</div>
            <div>
              <div style="font-size: 13px; font-weight: 700; color: #FFF;"><span class="code-pill">r-lg (16px)</span></div>
              <div style="font-size: 11px; color: var(--text-muted); margin-top: 2px;">기본 콘텐츠 카드, 모달 컨테이너</div>
            </div>
          </div>

          <div style="background: var(--bg-surface-2); padding: 14px; border-radius: 8px; display: flex; align-items: center; gap: 14px;">
            <div style="width: 50px; height: 50px; background: rgba(6,182,212,0.2); border: 1.5px solid var(--secondary); border-radius: 24px; display: flex; align-items: center; justify-content: center; font-size: 11px; font-family: 'JetBrains Mono', monospace; color: var(--secondary);">24px</div>
            <div>
              <div style="font-size: 13px; font-weight: 700; color: #FFF;"><span class="code-pill">r-xl (24px)</span></div>
              <div style="font-size: 11px; color: var(--text-muted); margin-top: 2px;">대형 패널, 대시보드 위젯</div>
            </div>
          </div>

          <div style="background: var(--bg-surface-2); padding: 14px; border-radius: 8px; display: flex; align-items: center; gap: 14px;">
            <div style="width: 50px; height: 50px; background: rgba(168,85,247,0.2); border: 1.5px solid var(--tertiary); border-radius: 9999px; display: flex; align-items: center; justify-content: center; font-size: 10px; font-family: 'JetBrains Mono', monospace; color: var(--tertiary);">FULL</div>
            <div>
              <div style="font-size: 13px; font-weight: 700; color: #FFF;"><span class="code-pill">r-full (9999px)</span></div>
              <div style="font-size: 11px; color: var(--text-muted); margin-top: 2px;">필(Pill) 버튼, 아바타, 라운드 뱃지</div>
            </div>
          </div>
        </div>
      </div>

      <!-- Shadow & Depth Effects -->
      <div class="card" style="padding: 20px;">
        <div style="font-size: 14px; font-weight: 700; color: #FFF; margin-bottom: 12px;">Shadow & Glow Effect Tokens</div>
        <div class="grid-3" style="gap: 16px;">
          <div style="background: var(--bg-surface-1); border: 1px solid var(--border-subtle); padding: 16px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0, 0, 0, 0.45);">
            <div style="font-size: 13px; font-weight: 700; color: #FFF;"><span class="code-pill">shadow-md</span></div>
            <div style="font-family: 'JetBrains Mono', monospace; font-size: 11px; color: var(--primary-light); margin: 6px 0;">0 4px 12px rgba(0,0,0,0.45)</div>
            <div style="font-size: 11px; color: var(--text-secondary);">표준 카드 및 드롭다운 메뉴 엘리베이션</div>
          </div>

          <div style="background: var(--bg-surface-1); border: 1px solid var(--border-subtle); padding: 16px; border-radius: 12px; box-shadow: 0 12px 32px rgba(0, 0, 0, 0.6);">
            <div style="font-size: 13px; font-weight: 700; color: #FFF;"><span class="code-pill">shadow-lg</span></div>
            <div style="font-family: 'JetBrains Mono', monospace; font-size: 11px; color: var(--primary-light); margin: 6px 0;">0 12px 32px rgba(0,0,0,0.6)</div>
            <div style="font-size: 11px; color: var(--text-secondary);">모달 대화상자, 플로팅 패널 엘리베이션</div>
          </div>

          <div style="background: var(--bg-surface-1); border: 1px solid rgba(99,102,241,0.5); padding: 16px; border-radius: 12px; box-shadow: 0 0 20px rgba(99, 102, 241, 0.4);">
            <div style="font-size: 13px; font-weight: 700; color: #FFF;"><span class="code-pill">glow-primary</span></div>
            <div style="font-family: 'JetBrains Mono', monospace; font-size: 11px; color: var(--secondary); margin: 6px 0;">0 0 20px rgba(99,102,241,0.4)</div>
            <div style="font-size: 11px; color: var(--text-secondary);">액티브 버튼, 선택된 퀴즈 카드 하이라이트</div>
          </div>
        </div>
      </div>
    </div>
    """
    return make_html(6, "FOUNDATIONS", "Radius & Effects (코너 라운드 & 이펙트)", "Border Radius & Elevation Shadows", "라운드 코너 규격 및 뎁스(Depth) 표현을 위한 그림자/글로우 이펙트 토큰", body)

def get_page_7():
    body = """
    <div style="display: flex; flex-direction: column; gap: 16px;">
      <div class="grid-3" style="gap: 16px;">
        <!-- Primary Button -->
        <div class="card" style="padding: 20px;">
          <div style="font-size: 14px; font-weight: 700; color: #FFF; margin-bottom: 12px; display: flex; justify-content: space-between;">
            <span>1. Primary Button</span>
            <span class="code-pill">CTA / Accent</span>
          </div>
          <div style="display: flex; flex-direction: column; gap: 10px;">
            <!-- Default -->
            <div style="background: var(--bg-surface-2); padding: 10px 14px; border-radius: 8px; display: flex; justify-content: space-between; align-items: center;">
              <span style="font-size: 11px; color: var(--text-muted); font-family: 'JetBrains Mono', monospace;">DEFAULT</span>
              <button style="height: 40px; padding: 0 20px; background: #6366F1; color: #FFF; font-weight: 600; font-size: 13px; border: none; border-radius: 10px; box-shadow: 0 4px 14px rgba(99,102,241,0.35); cursor: pointer;">
                시작하기 &rarr;
              </button>
            </div>
            <!-- Hover -->
            <div style="background: var(--bg-surface-2); padding: 10px 14px; border-radius: 8px; display: flex; justify-content: space-between; align-items: center;">
              <span style="font-size: 11px; color: var(--primary-light); font-family: 'JetBrains Mono', monospace;">HOVER</span>
              <button style="height: 40px; padding: 0 20px; background: #4F46E5; color: #FFF; font-weight: 600; font-size: 13px; border: none; border-radius: 10px; box-shadow: 0 0 20px rgba(99,102,241,0.6); transform: translateY(-1px); cursor: pointer;">
                시작하기 &rarr;
              </button>
            </div>
            <!-- Disabled -->
            <div style="background: var(--bg-surface-2); padding: 10px 14px; border-radius: 8px; display: flex; justify-content: space-between; align-items: center;">
              <span style="font-size: 11px; color: var(--text-muted); font-family: 'JetBrains Mono', monospace;">DISABLED</span>
              <button style="height: 40px; padding: 0 20px; background: #1F2937; color: #6B7280; font-weight: 600; font-size: 13px; border: 1px solid #374151; border-radius: 10px; opacity: 0.6; cursor: not-allowed;">
                시작하기 &rarr;
              </button>
            </div>
          </div>
        </div>

        <!-- Secondary Button -->
        <div class="card" style="padding: 20px;">
          <div style="font-size: 14px; font-weight: 700; color: #FFF; margin-bottom: 12px; display: flex; justify-content: space-between;">
            <span>2. Secondary / Outline</span>
            <span class="code-pill">Sub Action</span>
          </div>
          <div style="display: flex; flex-direction: column; gap: 10px;">
            <!-- Default -->
            <div style="background: var(--bg-surface-2); padding: 10px 14px; border-radius: 8px; display: flex; justify-content: space-between; align-items: center;">
              <span style="font-size: 11px; color: var(--text-muted); font-family: 'JetBrains Mono', monospace;">DEFAULT</span>
              <button style="height: 40px; padding: 0 20px; background: rgba(31,41,55,0.5); color: #F9FAFB; font-weight: 600; font-size: 13px; border: 1px solid rgba(255,255,255,0.15); border-radius: 10px; cursor: pointer;">
                상세보기
              </button>
            </div>
            <!-- Hover -->
            <div style="background: var(--bg-surface-2); padding: 10px 14px; border-radius: 8px; display: flex; justify-content: space-between; align-items: center;">
              <span style="font-size: 11px; color: var(--primary-light); font-family: 'JetBrains Mono', monospace;">HOVER</span>
              <button style="height: 40px; padding: 0 20px; background: rgba(255,255,255,0.08); color: #FFF; font-weight: 600; font-size: 13px; border: 1px solid #818CF8; border-radius: 10px; cursor: pointer;">
                상세보기
              </button>
            </div>
            <!-- Disabled -->
            <div style="background: var(--bg-surface-2); padding: 10px 14px; border-radius: 8px; display: flex; justify-content: space-between; align-items: center;">
              <span style="font-size: 11px; color: var(--text-muted); font-family: 'JetBrains Mono', monospace;">DISABLED</span>
              <button style="height: 40px; padding: 0 20px; background: transparent; color: #4B5563; font-weight: 600; font-size: 13px; border: 1px solid #2D3748; border-radius: 10px; cursor: not-allowed;">
                상세보기
              </button>
            </div>
          </div>
        </div>

        <!-- Ghost / Icon Button -->
        <div class="card" style="padding: 20px;">
          <div style="font-size: 14px; font-weight: 700; color: #FFF; margin-bottom: 12px; display: flex; justify-content: space-between;">
            <span>3. Ghost / Icon Button</span>
            <span class="code-pill">Tertiary</span>
          </div>
          <div style="display: flex; flex-direction: column; gap: 10px;">
            <!-- Default -->
            <div style="background: var(--bg-surface-2); padding: 10px 14px; border-radius: 8px; display: flex; justify-content: space-between; align-items: center;">
              <span style="font-size: 11px; color: var(--text-muted); font-family: 'JetBrains Mono', monospace;">DEFAULT</span>
              <button style="width: 40px; height: 40px; background: transparent; color: #9CA3AF; border: none; border-radius: 10px; font-size: 16px; cursor: pointer; display: flex; align-items: center; justify-content: center;">
                &#9881;
              </button>
            </div>
            <!-- Hover -->
            <div style="background: var(--bg-surface-2); padding: 10px 14px; border-radius: 8px; display: flex; justify-content: space-between; align-items: center;">
              <span style="font-size: 11px; color: var(--primary-light); font-family: 'JetBrains Mono', monospace;">HOVER</span>
              <button style="width: 40px; height: 40px; background: rgba(255,255,255,0.08); color: #FFF; border: none; border-radius: 10px; font-size: 16px; cursor: pointer; display: flex; align-items: center; justify-content: center;">
                &#9881;
              </button>
            </div>
            <!-- Disabled -->
            <div style="background: var(--bg-surface-2); padding: 10px 14px; border-radius: 8px; display: flex; justify-content: space-between; align-items: center;">
              <span style="font-size: 11px; color: var(--text-muted); font-family: 'JetBrains Mono', monospace;">DISABLED</span>
              <button style="width: 40px; height: 40px; background: transparent; color: #4B5563; border: none; border-radius: 10px; font-size: 16px; cursor: not-allowed; display: flex; align-items: center; justify-content: center;">
                &#9881;
              </button>
            </div>
          </div>
        </div>
      </div>

      <!-- Button Spec Table -->
      <div class="card" style="padding: 16px 20px;">
        <div style="font-size: 13px; font-weight: 700; color: #FFF; margin-bottom: 10px;">Button Specification Summary</div>
        <table class="spec-table">
          <thead>
            <tr>
              <th>VARIANT</th>
              <th>HEIGHT</th>
              <th>PADDING</th>
              <th>FONT SIZE & WEIGHT</th>
              <th>BACKGROUND</th>
              <th>BORDER / SHADOW</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong style="color: var(--primary-light);">Primary</strong></td>
              <td>48px (Large) / 40px (Medium)</td>
              <td>0 24px</td>
              <td>14px / SemiBold (600)</td>
              <td><span class="code-pill">#6366F1</span> (Hover: #4F46E5)</td>
              <td>Glow: 0 0 20px rgba(99,102,241,0.6)</td>
            </tr>
            <tr>
              <td><strong style="color: var(--text-primary);">Secondary</strong></td>
              <td>48px (Large) / 40px (Medium)</td>
              <td>0 20px</td>
              <td>14px / Medium (500)</td>
              <td><span class="code-pill">rgba(31,41,55,0.5)</span></td>
              <td>Border: 1px solid rgba(255,255,255,0.12)</td>
            </tr>
            <tr>
              <td><strong style="color: var(--text-muted);">Ghost / Icon</strong></td>
              <td>40px &times; 40px (Square)</td>
              <td>0</td>
              <td>16px Icon</td>
              <td><span class="code-pill">transparent</span></td>
              <td>Hover: rgba(255,255,255,0.06)</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    """
    return make_html(7, "COMPONENTS", "Button (버튼 시스템)", "Interactive Action Components", "Primary, Secondary, Ghost 버튼의 상태별(Default, Hover, Disabled) 명세", body)

def get_page_8():
    body = """
    <div style="display: flex; flex-direction: column; gap: 16px;">
      <!-- Common Spec Banner -->
      <div class="card" style="padding: 14px 20px; background: var(--bg-surface-2); display: flex; justify-content: space-between; align-items: center;">
        <div>
          <span style="font-weight: 700; color: #FFF; font-size: 13px;">Badge Common Specification:</span>
          <span style="font-size: 12px; color: var(--text-secondary); margin-left: 8px;">Height 26px &bull; Padding 3px 10px &bull; Radius 9999px (Pill) &bull; Font 12px SemiBold (600)</span>
        </div>
        <span class="code-pill">BORDER: 1PX SOLID</span>
      </div>

      <!-- Badge Gallery Grid -->
      <div class="grid-3" style="gap: 16px;">
        <!-- Success Badge -->
        <div class="card" style="padding: 18px; border-left: 3px solid var(--success);">
          <div style="font-size: 13px; font-weight: 700; color: #FFF; margin-bottom: 8px;">Success (완료 / 정답)</div>
          <div style="margin: 12px 0;">
            <span style="display: inline-flex; align-items: center; gap: 6px; height: 26px; padding: 0 12px; border-radius: 9999px; background: rgba(16, 185, 129, 0.12); border: 1px solid rgba(16, 185, 129, 0.35); color: #10B981; font-size: 12px; font-weight: 600;">
              <span style="width: 6px; height: 6px; border-radius: 50%; background: #10B981; box-shadow: 0 0 6px #10B981;"></span>
              정답 완료
            </span>
          </div>
          <div style="font-size: 11px; color: var(--text-muted); line-height: 1.5; font-family: 'JetBrains Mono', monospace;">
            BG: rgba(16, 185, 129, 0.12)<br>
            Border: rgba(16, 185, 129, 0.35)<br>
            Text: #10B981
          </div>
        </div>

        <!-- Warning Badge -->
        <div class="card" style="padding: 18px; border-left: 3px solid var(--warning);">
          <div style="font-size: 13px; font-weight: 700; color: #FFF; margin-bottom: 8px;">Warning (진행 중 / 임박)</div>
          <div style="margin: 12px 0;">
            <span style="display: inline-flex; align-items: center; gap: 6px; height: 26px; padding: 0 12px; border-radius: 9999px; background: rgba(245, 158, 11, 0.12); border: 1px solid rgba(245, 158, 11, 0.35); color: #F59E0B; font-size: 12px; font-weight: 600;">
              <span style="width: 6px; height: 6px; border-radius: 50%; background: #F59E0B; box-shadow: 0 0 6px #F59E0B;"></span>
              시간 임박
            </span>
          </div>
          <div style="font-size: 11px; color: var(--text-muted); line-height: 1.5; font-family: 'JetBrains Mono', monospace;">
            BG: rgba(245, 158, 11, 0.12)<br>
            Border: rgba(245, 158, 11, 0.35)<br>
            Text: #F59E0B
          </div>
        </div>

        <!-- Danger Badge -->
        <div class="card" style="padding: 18px; border-left: 3px solid var(--danger);">
          <div style="font-size: 13px; font-weight: 700; color: #FFF; margin-bottom: 8px;">Danger (실패 / 오답)</div>
          <div style="margin: 12px 0;">
            <span style="display: inline-flex; align-items: center; gap: 6px; height: 26px; padding: 0 12px; border-radius: 9999px; background: rgba(239, 68, 68, 0.12); border: 1px solid rgba(239, 68, 68, 0.35); color: #EF4444; font-size: 12px; font-weight: 600;">
              <span style="width: 6px; height: 6px; border-radius: 50%; background: #EF4444; box-shadow: 0 0 6px #EF4444;"></span>
              오답 확인
            </span>
          </div>
          <div style="font-size: 11px; color: var(--text-muted); line-height: 1.5; font-family: 'JetBrains Mono', monospace;">
            BG: rgba(239, 68, 68, 0.12)<br>
            Border: rgba(239, 68, 68, 0.35)<br>
            Text: #EF4444
          </div>
        </div>

        <!-- AI Accent Badge -->
        <div class="card" style="padding: 18px; border-left: 3px solid var(--tertiary);">
          <div style="font-size: 13px; font-weight: 700; color: #FFF; margin-bottom: 8px;">AI / Accent (인공지능 추천)</div>
          <div style="margin: 12px 0;">
            <span style="display: inline-flex; align-items: center; gap: 6px; height: 26px; padding: 0 12px; border-radius: 9999px; background: linear-gradient(135deg, rgba(99, 102, 241, 0.2), rgba(168, 85, 247, 0.2)); border: 1px solid rgba(129, 140, 248, 0.4); color: #A5B4FC; font-size: 12px; font-weight: 600; box-shadow: 0 0 12px rgba(99, 102, 241, 0.25);">
              &#10024; AI 분석
            </span>
          </div>
          <div style="font-size: 11px; color: var(--text-muted); line-height: 1.5; font-family: 'JetBrains Mono', monospace;">
            BG: Gradient (Indigo &rarr; Violet)<br>
            Border: rgba(129, 140, 248, 0.4)<br>
            Text: #A5B4FC
          </div>
        </div>

        <!-- Info / Category Badge -->
        <div class="card" style="padding: 18px; border-left: 3px solid var(--info);">
          <div style="font-size: 13px; font-weight: 700; color: #FFF; margin-bottom: 8px;">Info / Category (정보/안내)</div>
          <div style="margin: 12px 0;">
            <span style="display: inline-flex; align-items: center; gap: 6px; height: 26px; padding: 0 12px; border-radius: 9999px; background: rgba(59, 130, 246, 0.12); border: 1px solid rgba(59, 130, 246, 0.35); color: #3B82F6; font-size: 12px; font-weight: 600;">
              정보 안내
            </span>
          </div>
          <div style="font-size: 11px; color: var(--text-muted); line-height: 1.5; font-family: 'JetBrains Mono', monospace;">
            BG: rgba(59, 130, 246, 0.12)<br>
            Border: rgba(59, 130, 246, 0.35)<br>
            Text: #3B82F6
          </div>
        </div>

        <!-- Neutral Badge -->
        <div class="card" style="padding: 18px; border-left: 3px solid var(--text-muted);">
          <div style="font-size: 13px; font-weight: 700; color: #FFF; margin-bottom: 8px;">Neutral / System (일반 태그)</div>
          <div style="margin: 12px 0;">
            <span style="display: inline-flex; align-items: center; gap: 6px; height: 26px; padding: 0 12px; border-radius: 9999px; background: rgba(31, 41, 55, 0.6); border: 1px solid rgba(255, 255, 255, 0.12); color: #9CA3AF; font-size: 12px; font-weight: 600;">
              시스템 v1.0
            </span>
          </div>
          <div style="font-size: 11px; color: var(--text-muted); line-height: 1.5; font-family: 'JetBrains Mono', monospace;">
            BG: rgba(31, 41, 55, 0.6)<br>
            Border: rgba(255, 255, 255, 0.12)<br>
            Text: #9CA3AF
          </div>
        </div>
      </div>
    </div>
    """
    return make_html(8, "COMPONENTS", "Badge (상태 표시용 뱃지 스타일)", "Status & Indicator Badges", "상태 표시(Success, Warning, Danger, AI Accent) 뱃지 디자인 수치 및 스타일 명세", body)

def get_page_9():
    body = """
    <div style="display: flex; flex-direction: column; gap: 16px;">
      <!-- Linear Progress Bar -->
      <div class="card" style="padding: 20px;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px;">
          <div style="font-size: 14px; font-weight: 700; color: #FFF;">1. Linear Progress Bar System</div>
          <span class="code-pill">TRACK: 8PX HEIGHT &bull; GLOW: 10PX</span>
        </div>

        <div style="display: flex; flex-direction: column; gap: 14px;">
          <!-- 75% Active Bar -->
          <div>
            <div style="display: flex; justify-content: space-between; font-size: 12px; margin-bottom: 6px;">
              <span style="color: var(--text-primary); font-weight: 600;">전체 퀴즈 진행률</span>
              <span style="font-family: 'JetBrains Mono', monospace; color: var(--secondary); font-weight: 700;">75% (08/10 문항)</span>
            </div>
            <div style="height: 8px; width: 100%; background: #1F2937; border-radius: 9999px; overflow: hidden; position: relative;">
              <div style="height: 100%; width: 75%; background: linear-gradient(90deg, #6366F1 0%, #06B6D4 100%); border-radius: 9999px; box-shadow: 0 0 12px rgba(6, 182, 212, 0.6);"></div>
            </div>
          </div>

          <!-- 35% Bar -->
          <div>
            <div style="display: flex; justify-content: space-between; font-size: 12px; margin-bottom: 6px;">
              <span style="color: var(--text-primary); font-weight: 600;">섹션 1 학습 완료율</span>
              <span style="font-family: 'JetBrains Mono', monospace; color: var(--primary-light); font-weight: 700;">35%</span>
            </div>
            <div style="height: 8px; width: 100%; background: #1F2937; border-radius: 9999px; overflow: hidden;">
              <div style="height: 100%; width: 35%; background: linear-gradient(90deg, #6366F1, #818CF8); border-radius: 9999px;"></div>
            </div>
          </div>

          <!-- 100% Complete Bar -->
          <div>
            <div style="display: flex; justify-content: space-between; font-size: 12px; margin-bottom: 6px;">
              <span style="color: var(--text-primary); font-weight: 600;">최종 테스트 통과</span>
              <span style="font-family: 'JetBrains Mono', monospace; color: var(--success); font-weight: 700;">100% COMPLETED</span>
            </div>
            <div style="height: 8px; width: 100%; background: #1F2937; border-radius: 9999px; overflow: hidden;">
              <div style="height: 100%; width: 100%; background: #10B981; border-radius: 9999px; box-shadow: 0 0 12px rgba(16, 185, 129, 0.5);"></div>
            </div>
          </div>
        </div>
      </div>

      <!-- Stepped Progress Indicator -->
      <div class="card" style="padding: 20px;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">
          <div style="font-size: 14px; font-weight: 700; color: #FFF;">2. Stepped Progress Indicator (단계형 인디케이터)</div>
          <span class="code-pill">NODE: 32PX &times; 32PX</span>
        </div>

        <div style="display: flex; align-items: center; justify-content: space-between; position: relative; padding: 10px 20px;">
          <!-- Step 1: Completed -->
          <div style="display: flex; flex-direction: column; align-items: center; gap: 8px; z-index: 2;">
            <div style="width: 32px; height: 32px; border-radius: 50%; background: #10B981; color: #FFF; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 14px; box-shadow: 0 0 12px rgba(16, 185, 129, 0.4);">&#10003;</div>
            <div style="font-size: 11px; color: #10B981; font-weight: 600;">1단계 완료</div>
          </div>

          <div style="flex: 1; height: 2px; background: #10B981; margin: 0 8px; margin-bottom: 24px;"></div>

          <!-- Step 2: Completed -->
          <div style="display: flex; flex-direction: column; align-items: center; gap: 8px; z-index: 2;">
            <div style="width: 32px; height: 32px; border-radius: 50%; background: #10B981; color: #FFF; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 14px; box-shadow: 0 0 12px rgba(16, 185, 129, 0.4);">&#10003;</div>
            <div style="font-size: 11px; color: #10B981; font-weight: 600;">2단계 완료</div>
          </div>

          <div style="flex: 1; height: 2px; background: linear-gradient(90deg, #10B981, #6366F1); margin: 0 8px; margin-bottom: 24px;"></div>

          <!-- Step 3: Active -->
          <div style="display: flex; flex-direction: column; align-items: center; gap: 8px; z-index: 2;">
            <div style="width: 32px; height: 32px; border-radius: 50%; background: #6366F1; color: #FFF; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 14px; box-shadow: 0 0 16px rgba(99, 102, 241, 0.7); border: 2px solid #818CF8;">3</div>
            <div style="font-size: 11px; color: var(--primary-light); font-weight: 700;">3단계 진행 중</div>
          </div>

          <div style="flex: 1; height: 2px; background: #1F2937; margin: 0 8px; margin-bottom: 24px;"></div>

          <!-- Step 4: Upcoming -->
          <div style="display: flex; flex-direction: column; align-items: center; gap: 8px; z-index: 2;">
            <div style="width: 32px; height: 32px; border-radius: 50%; background: #111827; border: 1px solid #374151; color: #6B7280; display: flex; align-items: center; justify-content: center; font-weight: 600; font-size: 13px;">4</div>
            <div style="font-size: 11px; color: #6B7280;">4단계 대기</div>
          </div>

          <div style="flex: 1; height: 2px; background: #1F2937; margin: 0 8px; margin-bottom: 24px;"></div>

          <!-- Step 5: Upcoming -->
          <div style="display: flex; flex-direction: column; align-items: center; gap: 8px; z-index: 2;">
            <div style="width: 32px; height: 32px; border-radius: 50%; background: #111827; border: 1px solid #374151; color: #6B7280; display: flex; align-items: center; justify-content: center; font-weight: 600; font-size: 13px;">5</div>
            <div style="font-size: 11px; color: #6B7280;">5단계 결과</div>
          </div>
        </div>
      </div>
    </div>
    """
    return make_html(9, "COMPONENTS", "Progress (프로그레스 바 디자인 수치)", "Linear & Stepped Progress Bar", "리니어 프로그레스 바(Glow 그라디언트) 및 5단계 스텝 인디케이터 수치 명세", body)

def get_page_10():
    body = """
    <div style="display: flex; flex-direction: column; gap: 16px;">
      <!-- Main Question Tracker Badge -->
      <div class="card" style="padding: 20px;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px;">
          <div style="font-size: 14px; font-weight: 700; color: #FFF;">1. Main Question Tracker Badge</div>
          <span class="code-pill">CONTAINER: H 36PX &bull; RADIUS 8PX</span>
        </div>

        <div style="display: flex; gap: 20px; align-items: center;">
          <!-- Visual Badge -->
          <div style="display: inline-flex; align-items: center; gap: 10px; height: 36px; padding: 0 16px; background: rgba(31, 41, 55, 0.8); border: 1px solid rgba(99, 102, 241, 0.4); border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.3);">
            <span style="font-size: 11px; font-weight: 800; color: var(--primary-light); letter-spacing: 0.1em; font-family: 'JetBrains Mono', monospace;">QUESTION</span>
            <span style="color: rgba(255,255,255,0.2);">|</span>
            <span style="font-family: 'JetBrains Mono', monospace; font-size: 15px; font-weight: 800; color: #FFFFFF;">03 <span style="color: #6B7280; font-size: 13px; font-weight: 500;">/ 10</span></span>
          </div>

          <!-- Explanations -->
          <div style="font-size: 12px; color: var(--text-secondary); line-height: 1.5;">
            &bull; Prefix Tag: <span class="code-pill">QUESTION</span> (11px Bold, Tracking 0.1em, #818CF8)<br>
            &bull; Current / Total Counter: <span class="code-pill">03 / 10</span> (15px JetBrains Mono Bold, #FFFFFF / #6B7280)
          </div>
        </div>
      </div>

      <!-- Pagination Question Pills -->
      <div class="card" style="padding: 20px;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px;">
          <div style="font-size: 14px; font-weight: 700; color: #FFF;">2. Pagination Question Number Pills (1 ~ 10 문항 내비게이션)</div>
          <span class="code-pill">SIZE: 36PX &times; 36PX &bull; RADIUS 10PX</span>
        </div>

        <div style="display: flex; gap: 10px; align-items: center; margin: 10px 0;">
          <!-- 1: Answered Correct -->
          <div style="width: 36px; height: 36px; border-radius: 10px; background: rgba(16, 185, 129, 0.15); border: 1px solid #10B981; color: #10B981; display: flex; align-items: center; justify-content: center; font-family: 'JetBrains Mono', monospace; font-weight: 700; font-size: 13px;">1</div>
          <!-- 2: Answered Correct -->
          <div style="width: 36px; height: 36px; border-radius: 10px; background: rgba(16, 185, 129, 0.15); border: 1px solid #10B981; color: #10B981; display: flex; align-items: center; justify-content: center; font-family: 'JetBrains Mono', monospace; font-weight: 700; font-size: 13px;">2</div>
          <!-- 3: Current Active -->
          <div style="width: 36px; height: 36px; border-radius: 10px; background: #6366F1; border: 1px solid #818CF8; color: #FFFFFF; display: flex; align-items: center; justify-content: center; font-family: 'JetBrains Mono', monospace; font-weight: 700; font-size: 14px; box-shadow: 0 0 16px rgba(99, 102, 241, 0.7);">3</div>
          <!-- 4: Unanswered -->
          <div style="width: 36px; height: 36px; border-radius: 10px; background: #111827; border: 1px solid #1F2937; color: #9CA3AF; display: flex; align-items: center; justify-content: center; font-family: 'JetBrains Mono', monospace; font-weight: 600; font-size: 13px;">4</div>
          <!-- 5: Unanswered -->
          <div style="width: 36px; height: 36px; border-radius: 10px; background: #111827; border: 1px solid #1F2937; color: #9CA3AF; display: flex; align-items: center; justify-content: center; font-family: 'JetBrains Mono', monospace; font-weight: 600; font-size: 13px;">5</div>
          <!-- 6: Unanswered -->
          <div style="width: 36px; height: 36px; border-radius: 10px; background: #111827; border: 1px solid #1F2937; color: #9CA3AF; display: flex; align-items: center; justify-content: center; font-family: 'JetBrains Mono', monospace; font-weight: 600; font-size: 13px;">6</div>
          <!-- 7: Unanswered -->
          <div style="width: 36px; height: 36px; border-radius: 10px; background: #111827; border: 1px solid #1F2937; color: #9CA3AF; display: flex; align-items: center; justify-content: center; font-family: 'JetBrains Mono', monospace; font-weight: 600; font-size: 13px;">7</div>
          <!-- 8: Unanswered -->
          <div style="width: 36px; height: 36px; border-radius: 10px; background: #111827; border: 1px solid #1F2937; color: #9CA3AF; display: flex; align-items: center; justify-content: center; font-family: 'JetBrains Mono', monospace; font-weight: 600; font-size: 13px;">8</div>
          <!-- 9: Unanswered -->
          <div style="width: 36px; height: 36px; border-radius: 10px; background: #111827; border: 1px solid #1F2937; color: #9CA3AF; display: flex; align-items: center; justify-content: center; font-family: 'JetBrains Mono', monospace; font-weight: 600; font-size: 13px;">9</div>
          <!-- 10: Unanswered -->
          <div style="width: 36px; height: 36px; border-radius: 10px; background: #111827; border: 1px solid #1F2937; color: #9CA3AF; display: flex; align-items: center; justify-content: center; font-family: 'JetBrains Mono', monospace; font-weight: 600; font-size: 13px;">10</div>
        </div>

        <div class="grid-3" style="gap: 12px; margin-top: 14px;">
          <div style="background: var(--bg-surface-2); padding: 10px 14px; border-radius: 8px; font-size: 12px;">
            <strong style="color: var(--primary-light);">Current (현재 문항):</strong><br>
            <span style="color: var(--text-secondary);">BG #6366F1 &bull; Text #FFF &bull; Glow 16px</span>
          </div>
          <div style="background: var(--bg-surface-2); padding: 10px 14px; border-radius: 8px; font-size: 12px;">
            <strong style="color: var(--success);">Answered (답변 완료):</strong><br>
            <span style="color: var(--text-secondary);">BG rgba(16,185,129,0.15) &bull; Border #10B981</span>
          </div>
          <div style="background: var(--bg-surface-2); padding: 10px 14px; border-radius: 8px; font-size: 12px;">
            <strong style="color: var(--text-muted);">Unanswered (미답변):</strong><br>
            <span style="color: var(--text-secondary);">BG #111827 &bull; Border #1F2937 &bull; Text #9CA3AF</span>
          </div>
        </div>
      </div>
    </div>
    """
    return make_html(10, "COMPONENTS", "Question Number (질문 번호 인디케이터)", "Quiz Question Tracker & Pagination", "질문 번호 트래커 뱃지 및 10개 문항 내비게이션 상태별(Active, Answered, Unanswered) 명세", body)

def get_page_11():
    body = """
    <div style="display: flex; flex-direction: column; gap: 14px;">
      <div style="font-size: 13px; color: var(--text-secondary); margin-bottom: 2px;">
        퀴즈 선택지 카드는 <span class="code-pill">Height 56px</span>, <span class="code-pill">Radius 12px</span>, <span class="code-pill">Padding 0 16px</span> 규격으로 설계되었으며 5가지 인터랙션 상태를 지원합니다.
      </div>

      <!-- 5 Option States -->
      <div style="display: flex; flex-direction: column; gap: 8px;">
        <!-- 1. Default State -->
        <div style="height: 52px; background: #111827; border: 1px solid #1F2937; border-radius: 12px; padding: 0 16px; display: flex; align-items: center; justify-content: space-between;">
          <div style="display: flex; align-items: center; gap: 14px;">
            <div style="width: 28px; height: 28px; border-radius: 6px; background: #1F2937; color: #9CA3AF; display: flex; align-items: center; justify-content: center; font-family: 'JetBrains Mono', monospace; font-weight: 700; font-size: 13px;">A</div>
            <span style="font-size: 14px; color: #E5E7EB; font-weight: 500;">기본 미선택 상태 (Default State) — 다크 서피스 1 기반</span>
          </div>
          <span class="code-pill">DEFAULT</span>
        </div>

        <!-- 2. Hover State -->
        <div style="height: 52px; background: #161F30; border: 1px solid #6366F1; border-radius: 12px; padding: 0 16px; display: flex; align-items: center; justify-content: space-between; box-shadow: 0 4px 16px rgba(0, 0, 0, 0.4);">
          <div style="display: flex; align-items: center; gap: 14px;">
            <div style="width: 28px; height: 28px; border-radius: 6px; background: rgba(99, 102, 241, 0.2); color: #818CF8; display: flex; align-items: center; justify-content: center; font-family: 'JetBrains Mono', monospace; font-weight: 700; font-size: 13px;">B</div>
            <span style="font-size: 14px; color: #FFFFFF; font-weight: 500;">마우스 호버 상태 (Hover State) — 인디고 보더 하이라이트</span>
          </div>
          <span class="code-pill" style="color: var(--primary-light);">HOVER</span>
        </div>

        <!-- 3. Selected State -->
        <div style="height: 52px; background: rgba(99, 102, 241, 0.12); border: 1.5px solid #6366F1; border-radius: 12px; padding: 0 16px; display: flex; align-items: center; justify-content: space-between; box-shadow: 0 0 16px rgba(99, 102, 241, 0.25);">
          <div style="display: flex; align-items: center; gap: 14px;">
            <div style="width: 28px; height: 28px; border-radius: 6px; background: #6366F1; color: #FFFFFF; display: flex; align-items: center; justify-content: center; font-family: 'JetBrains Mono', monospace; font-weight: 700; font-size: 13px;">C</div>
            <span style="font-size: 14px; color: #FFFFFF; font-weight: 600;">사용자 선택 상태 (Selected State) — 인디고 채움 및 글로우</span>
          </div>
          <span class="code-pill" style="color: var(--primary-light); background: rgba(99,102,241,0.2);">SELECTED</span>
        </div>

        <!-- 4. Correct State -->
        <div style="height: 52px; background: rgba(16, 185, 129, 0.12); border: 1.5px solid #10B981; border-radius: 12px; padding: 0 16px; display: flex; align-items: center; justify-content: space-between; box-shadow: 0 0 16px rgba(16, 185, 129, 0.25);">
          <div style="display: flex; align-items: center; gap: 14px;">
            <div style="width: 28px; height: 28px; border-radius: 6px; background: #10B981; color: #FFFFFF; display: flex; align-items: center; justify-content: center; font-family: 'JetBrains Mono', monospace; font-weight: 700; font-size: 13px;">&#10003;</div>
            <span style="font-size: 14px; color: #FFFFFF; font-weight: 600;">정답 피드백 상태 (Correct Answer) — 그린 하이라이트</span>
          </div>
          <span class="code-pill" style="color: var(--success); background: rgba(16,185,129,0.2);">CORRECT</span>
        </div>

        <!-- 5. Incorrect State -->
        <div style="height: 52px; background: rgba(239, 68, 68, 0.12); border: 1.5px solid #EF4444; border-radius: 12px; padding: 0 16px; display: flex; align-items: center; justify-content: space-between;">
          <div style="display: flex; align-items: center; gap: 14px;">
            <div style="width: 28px; height: 28px; border-radius: 6px; background: #EF4444; color: #FFFFFF; display: flex; align-items: center; justify-content: center; font-family: 'JetBrains Mono', monospace; font-weight: 700; font-size: 13px;">&#10007;</div>
            <span style="font-size: 14px; color: #FCA5A5; font-weight: 500;">오답 피드백 상태 (Incorrect Answer) — 레드 경고 표시</span>
          </div>
          <span class="code-pill" style="color: var(--danger); background: rgba(239,68,68,0.2);">INCORRECT</span>
        </div>
      </div>
    </div>
    """
    return make_html(11, "COMPONENTS", "Quiz Option (퀴즈 선택지 카드/리스트 스타일)", "Quiz Option Interaction States", "퀴즈 선택지 카드 5단계 상태(Default, Hover, Selected, Correct, Incorrect) 상세 명세", body)

def get_page_12():
    body = """
    <div style="display: flex; flex-direction: column; gap: 16px;">
      <div class="grid-2" style="gap: 16px;">
        <!-- Compact Timer Badge -->
        <div class="card" style="padding: 20px;">
          <div style="font-size: 14px; font-weight: 700; color: #FFF; margin-bottom: 12px; display: flex; justify-content: space-between;">
            <span>1. Compact Timer Badge</span>
            <span class="code-pill">HEADER COMPONENT</span>
          </div>

          <div style="display: flex; flex-direction: column; gap: 14px;">
            <!-- Normal State -->
            <div style="background: var(--bg-surface-2); padding: 12px 16px; border-radius: 10px; display: flex; justify-content: space-between; align-items: center;">
              <div>
                <div style="font-size: 12px; font-weight: 700; color: #FFF;">정상 시간 (Normal State &gt; 10s)</div>
                <div style="font-size: 11px; color: var(--text-muted);">안정적인 시안 글로우 인디케이터</div>
              </div>
              <div style="display: inline-flex; align-items: center; gap: 8px; height: 34px; padding: 0 14px; background: #111827; border: 1px solid rgba(6, 182, 212, 0.4); border-radius: 9999px;">
                <span style="color: var(--secondary); font-size: 14px;">&#9201;</span>
                <span style="font-family: 'JetBrains Mono', monospace; font-size: 14px; font-weight: 700; color: #F9FAFB;">00:45</span>
              </div>
            </div>

            <!-- Warning/Danger State -->
            <div style="background: var(--bg-surface-2); padding: 12px 16px; border-radius: 10px; display: flex; justify-content: space-between; align-items: center;">
              <div>
                <div style="font-size: 12px; font-weight: 700; color: #EF4444;">임박 시간 (Danger State &le; 10s)</div>
                <div style="font-size: 11px; color: var(--text-muted);">레드 펄스 애니메이션 및 경고 글로우</div>
              </div>
              <div style="display: inline-flex; align-items: center; gap: 8px; height: 34px; padding: 0 14px; background: rgba(239,68,68,0.15); border: 1px solid #EF4444; border-radius: 9999px; box-shadow: 0 0 12px rgba(239,68,68,0.4);">
                <span style="color: #EF4444; font-size: 14px;">&#9201;</span>
                <span style="font-family: 'JetBrains Mono', monospace; font-size: 14px; font-weight: 700; color: #EF4444;">00:08</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Circular Gauge Timer -->
        <div class="card" style="padding: 20px;">
          <div style="font-size: 14px; font-weight: 700; color: #FFF; margin-bottom: 12px; display: flex; justify-content: space-between;">
            <span>2. Circular Gauge Timer</span>
            <span class="code-pill">96PX &times; 96PX</span>
          </div>

          <div style="display: flex; gap: 24px; align-items: center; justify-content: center; padding: 10px 0;">
            <!-- Normal Circular Timer -->
            <div style="display: flex; flex-direction: column; align-items: center; gap: 8px;">
              <div style="width: 80px; height: 80px; border-radius: 50%; background: conic-gradient(#06B6D4 0% 75%, #1F2937 75% 100%); display: flex; align-items: center; justify-content: center; box-shadow: 0 0 16px rgba(6, 182, 212, 0.4);">
                <div style="width: 66px; height: 66px; border-radius: 50%; background: #111827; display: flex; align-items: center; justify-content: center; font-family: 'JetBrains Mono', monospace; font-size: 14px; font-weight: 700; color: #FFF;">
                  00:45
                </div>
              </div>
              <div style="font-size: 11px; color: var(--secondary); font-weight: 600;">Normal (75%)</div>
            </div>

            <!-- Danger Circular Timer -->
            <div style="display: flex; flex-direction: column; align-items: center; gap: 8px;">
              <div style="width: 80px; height: 80px; border-radius: 50%; background: conic-gradient(#EF4444 0% 15%, #1F2937 15% 100%); display: flex; align-items: center; justify-content: center; box-shadow: 0 0 16px rgba(239, 68, 68, 0.5);">
                <div style="width: 66px; height: 66px; border-radius: 50%; background: #111827; display: flex; align-items: center; justify-content: center; font-family: 'JetBrains Mono', monospace; font-size: 14px; font-weight: 700; color: #EF4444;">
                  00:08
                </div>
              </div>
              <div style="font-size: 11px; color: var(--danger); font-weight: 600;">Danger (15%)</div>
            </div>
          </div>
        </div>
      </div>

      <!-- Linear Countdown Bar -->
      <div class="card" style="padding: 16px 20px;">
        <div style="font-size: 13px; font-weight: 700; color: #FFF; margin-bottom: 8px;">3. Linear Countdown Bar (상단 진행 바)</div>
        <div style="height: 6px; width: 100%; background: #1F2937; border-radius: 9999px; overflow: hidden;">
          <div style="height: 100%; width: 70%; background: linear-gradient(90deg, #6366F1, #06B6D4); box-shadow: 0 0 10px rgba(6,182,212,0.6);"></div>
        </div>
        <div style="display: flex; justify-content: space-between; font-size: 11px; color: var(--text-muted); margin-top: 6px; font-family: 'JetBrains Mono', monospace;">
          <span>TOTAL TIME: 60s</span>
          <span>REMAINING: 42s (70%)</span>
        </div>
      </div>
    </div>
    """
    return make_html(12, "COMPONENTS", "Timer (타이머 UI 디자인)", "Quiz & Assessment Timer Components", "컴팩트 뱃지 타이머, 원형 게이지 타이머(정상/경고 상태) UI 수치 명세", body)

def get_page_13():
    body = """
    <div style="display: flex; flex-direction: column; gap: 16px;">
      <div class="grid-3" style="gap: 16px;">
        <!-- 1. Standard Content Card -->
        <div class="card card-highlight" style="padding: 20px; display: flex; flex-direction: column; justify-content: space-between; height: 260px;">
          <div>
            <!-- Header -->
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
              <span style="display: inline-flex; align-items: center; height: 22px; padding: 0 8px; border-radius: 9999px; background: rgba(99,102,241,0.15); color: var(--primary-light); font-size: 11px; font-weight: 600;">
                AI & SaaS
              </span>
              <span style="color: var(--text-muted); font-size: 14px;">&#9734;</span>
            </div>
            <!-- Body -->
            <div style="font-size: 16px; font-weight: 700; color: #FFF; margin-bottom: 6px;">네오 테크 디자인 시스템</div>
            <div style="font-size: 12px; color: var(--text-secondary); line-height: 1.5;">
              딥 다크 캔버스와 고대비 인디고 포인트를 결합한 차세대 엔터프라이즈 UI 컴포넌트 라이브러리.
            </div>
          </div>
          <!-- Footer -->
          <div style="border-top: 1px solid var(--border-subtle); padding-top: 10px; display: flex; justify-content: space-between; align-items: center;">
            <span style="font-family: 'JetBrains Mono', monospace; font-size: 11px; color: var(--text-muted);">12개 컴포넌트</span>
            <button style="height: 28px; padding: 0 12px; background: #6366F1; color: #FFF; font-size: 11px; font-weight: 600; border: none; border-radius: 6px; cursor: pointer;">열기</button>
          </div>
        </div>

        <!-- 2. Interactive Elevated Card (Hover) -->
        <div class="card-elevated card-highlight" style="padding: 20px; display: flex; flex-direction: column; justify-content: space-between; height: 260px; border: 1px solid rgba(99, 102, 241, 0.4); box-shadow: 0 16px 36px rgba(0, 0, 0, 0.6), 0 0 20px rgba(99, 102, 241, 0.2); transform: translateY(-2px);">
          <div>
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
              <span style="display: inline-flex; align-items: center; height: 22px; padding: 0 8px; border-radius: 9999px; background: rgba(6,182,212,0.15); color: var(--secondary); font-size: 11px; font-weight: 600;">
                ACTIVE HOVER
              </span>
              <span style="color: var(--primary-light); font-size: 14px;">&#9733;</span>
            </div>
            <div style="font-size: 16px; font-weight: 700; color: #FFF; margin-bottom: 6px;">엘리베이트 인터랙티브 카드</div>
            <div style="font-size: 12px; color: var(--text-secondary); line-height: 1.5;">
              호버 시 <span class="code-pill">translateY(-2px)</span> 및 인디고 앰비언트 글로우가 활성화되어 물리적 반응감을 제공합니다.
            </div>
          </div>
          <div style="border-top: 1px solid var(--border-subtle); padding-top: 10px; display: flex; justify-content: space-between; align-items: center;">
            <span style="font-family: 'JetBrains Mono', monospace; font-size: 11px; color: var(--secondary);">ELEVATION L2</span>
            <button style="height: 28px; padding: 0 12px; background: #4F46E5; color: #FFF; font-size: 11px; font-weight: 600; border: none; border-radius: 6px; cursor: pointer;">선택됨</button>
          </div>
        </div>

        <!-- 3. Stats / Metric Card -->
        <div class="card" style="padding: 20px; display: flex; flex-direction: column; justify-content: space-between; height: 260px; border-top: 3px solid var(--tertiary);">
          <div>
            <div style="font-family: 'JetBrains Mono', monospace; font-size: 11px; color: var(--text-muted);">TOTAL COMPLETION</div>
            <div style="font-size: 32px; font-weight: 800; color: #FFF; font-family: 'JetBrains Mono', monospace; margin: 6px 0;">98.4%</div>
            <div style="display: inline-flex; align-items: center; gap: 4px; font-size: 11px; color: var(--success); background: rgba(16,185,129,0.12); padding: 2px 8px; border-radius: 4px;">
              &uarr; +14.2% 지난주 대비
            </div>
          </div>
          <div style="border-top: 1px solid var(--border-subtle); padding-top: 10px;">
            <div style="font-size: 11px; color: var(--text-muted); line-height: 1.4;">
              엄격한 8pt 그리드와 토큰 시스템을 통해 렌더링 일관성 100% 달성.
            </div>
          </div>
        </div>
      </div>

      <!-- Card Specs Table -->
      <div class="card" style="padding: 14px 20px;">
        <div style="font-size: 13px; font-weight: 700; color: #FFF; margin-bottom: 8px;">Card Layout & Hierarchy Specification</div>
        <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; font-size: 11px;">
          <div><strong style="color: var(--primary-light);">Background:</strong> #111827 (Surface 1)</div>
          <div><strong style="color: var(--primary-light);">Border:</strong> 1px rgba(255,255,255,0.08)</div>
          <div><strong style="color: var(--primary-light);">Radius:</strong> 16px (r-lg)</div>
          <div><strong style="color: var(--primary-light);">Padding:</strong> 20px ~ 24px</div>
        </div>
      </div>
    </div>
    """
    return make_html(13, "COMPONENTS", "Card (기본 콘텐츠 카드 레이아웃 및 스타일)", "Content Container & Card Hierarchy", "기본 콘텐츠 카드, 인터랙티브 엘리베이트 카드, 통계 메트릭 카드 레이아웃 명세", body)

PAGES = [
    get_page_1, get_page_2, get_page_3, get_page_4, get_page_5,
    get_page_6, get_page_7, get_page_8, get_page_9, get_page_10,
    get_page_11, get_page_12, get_page_13
]

def generate_all():
    print(f"Starting generation of 13 Style Guide Draft PNGs...")
    print(f"Target Directory: {OUTPUT_DIR}")
    print(f"Browser Engine: {CHROME_PATH}")

    with tempfile.TemporaryDirectory() as tmp_dir:
        for idx, page_func in enumerate(PAGES, start=1):
            html_content = page_func()
            html_path = Path(tmp_dir) / f"page_{idx}.html"
            html_path.write_text(html_content, encoding="utf-8")
            
            output_png = OUTPUT_DIR / f"스타일가이드_초안{idx}.png"
            
            cmd = [
                CHROME_PATH,
                "--headless=new",
                "--disable-gpu",
                "--no-sandbox",
                "--hide-scrollbars",
                "--window-size=1600,1000",
                f"--screenshot={str(output_png)}",
                str(html_path.resolve().as_uri())
            ]
            
            res = subprocess.run(cmd, capture_output=True, text=True)
            if output_png.exists() and output_png.stat().st_size > 0:
                print(f"[{idx}/13] Successfully generated: {output_png.name} ({output_png.stat().st_size:,} bytes)")
            else:
                print(f"[{idx}/13] Failed to generate: {output_png.name}. Error: {res.stderr}")

if __name__ == "__main__":
    generate_all()
