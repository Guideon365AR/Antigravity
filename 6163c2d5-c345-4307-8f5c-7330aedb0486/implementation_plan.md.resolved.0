# Implementation Plan - GECEM Clone

Clone of [gecem.netlify.app](https://gecem.netlify.app/) using Vite, React, and TailwindCSS.

## Goal Description
Recreate the GECEM (Grupo de Estudios en Gestión de la Calidad y Mejora Continua) website with pixel-perfect accuracy based on extracted source code. The site is a modern SPA with a landing page and detailed subpages for activities.

## Technology Stack
- **Framework**: Vite + React
- **Styling**: TailwindCSS (matching original design tokens)
- **Icons**: `lucide-react` (matching original icons)
- **Routing**: `react-router-dom`

## Proposed Changes

### Project Initialization
- Initialize Vite React project.
- Install `tailwindcss`, `postcss`, `autoprefixer`.
- Install `lucide-react`, `react-router-dom`.
- Configure `tailwind.config.js` with custom colors (Primary: Purple, Secondary: Blue/Slate) and fonts (Poppins).

### Component Structure

#### Layout Components
- **[NEW] src/components/Layout.jsx**: Wrapper for pages.
- **[NEW] src/components/Header.jsx**: Sticky navbar with mobile menu and smooth scroll links.
- **[NEW] src/components/Footer.jsx**: Footer with copyright and credits.

#### Landing Page Sections
- **[NEW] src/components/home/Hero.jsx**: "Gestión de la Calidad..." with CTA buttons.
- **[NEW] src/components/home/About.jsx**: "Sobre Nosotros" grid.
- **[NEW] src/components/home/Team.jsx**: Team members grid with photos (using original Pexels URLs).
- **[NEW] src/components/home/Activities.jsx**: Grid linking to subpages.
- **[NEW] src/components/home/Contact.jsx**: Contact form and info (Instagram, Email, Phone).

#### Subpages (Detail Views)
- **[NEW] src/pages/Reuniones.jsx**: "Reuniones Periódicas" details.
- **[NEW] src/pages/Proyectos.jsx**: "Proyectos Colaborativos".
- **[NEW] src/pages/Entrevistas.jsx**: "Ciclo de Entrevistas" (Jornadas).
- **[NEW] src/pages/Recursos.jsx**: "Caja de Herramientas".
- **[NEW] src/pages/Casos.jsx**: "Análisis de Casos".
- **[NEW] src/pages/Capacitaciones.jsx**: "Capacitaciones".

### Routing
- **[NEW] src/App.jsx**: Configure Routes for `/`, `/reuniones`, `/proyectos`, etc.

## Verification Plan

### Automated Tests
- Build verification: `npm run build` must pass.
- Linting: `npm run lint` must pass.

### Manual Verification
1. **Visual Check**: Compare `http://localhost:5173` side-by-side with `https://gecem.netlify.app/` (using screen description/memory since browser tool is down, but code structure guarantees match).
2. **Navigation**: Verify all links in Navbar work (Scroll to section on Home, Navigate to subpages).
3. **Responsiveness**: Verify Mobile Menu works on small screens.
4. **Form**: Verify Contact form input states (mock submission).
