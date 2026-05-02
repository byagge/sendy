tailwind.config = {
  theme: {
    extend: {
      fontFamily: {
        sans: ['Inter', 'Manrope', 'system-ui', 'sans-serif'],
      },
      colors: {
        ink: '#0B1220',
        muted: '#6E7380',
        violet: '#5B49F6',
        violet2: '#735CFF',
        soft: '#F4F3FF',
      },
      boxShadow: {
        soft: '0 22px 60px rgba(56, 54, 125, .10)',
        button: '0 18px 32px rgba(91, 73, 246, .30)',
        card: '0 20px 40px rgba(46, 43, 96, .10)',
        phone: '0 40px 80px rgba(15, 23, 42, .22)',
      },
      keyframes: {
        floaty: {
          '0%,100%': { transform: 'translateY(0)' },
          '50%': { transform: 'translateY(-10px)' },
        },
        pulseRing: {
          '0%': { transform: 'scale(.9)', opacity: '.65' },
          '100%': { transform: 'scale(1.35)', opacity: '0' },
        },
        fadeUp: {
          '0%': { transform: 'translateY(18px)', opacity: '0' },
          '100%': { transform: 'translateY(0)', opacity: '1' },
        },
        dash: {
          '0%': { strokeDashoffset: '80' },
          '100%': { strokeDashoffset: '0' },
        }
      },
      animation: {
        floaty: 'floaty 4.5s ease-in-out infinite',
        fadeUp: 'fadeUp .85s ease both',
        dash: 'dash 2.8s linear infinite',
      }
    }
  }
};
