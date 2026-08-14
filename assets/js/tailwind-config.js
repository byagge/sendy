tailwind.config = {
  theme: {
    extend: {
      fontFamily: {
        sans: ['Plus Jakarta Sans', 'Manrope', 'system-ui', 'sans-serif'],
        display: ['Fraunces', 'Georgia', 'serif'],
      },
      colors: {
        ink: '#161310',
        muted: '#6B645C',
        pine: '#0F4F46',
        pine2: '#167A6F',
        glow: '#2BB5A5',
        sand: '#F3EDE3',
        mist: '#FAF7F2',
        gold: '#C7923A',
      },
      boxShadow: {
        soft: '0 22px 60px rgba(22, 19, 16, .08)',
        button: '0 16px 34px rgba(15, 79, 70, .28)',
        card: '0 18px 44px rgba(22, 19, 16, .08)',
        lift: '0 28px 64px rgba(15, 79, 70, .14)',
      },
      keyframes: {
        floaty: {
          '0%,100%': { transform: 'translateY(0)' },
          '50%': { transform: 'translateY(-10px)' },
        },
        pulseRing: {
          '0%': { transform: 'scale(.9)', opacity: '.65' },
          '100%': { transform: 'scale(1.4)', opacity: '0' },
        },
        fadeUp: {
          '0%': { transform: 'translateY(22px)', opacity: '0' },
          '100%': { transform: 'translateY(0)', opacity: '1' },
        },
        marquee: {
          '0%': { transform: 'translateX(0)' },
          '100%': { transform: 'translateX(-50%)' },
        },
        dash: {
          '0%': { strokeDashoffset: '80' },
          '100%': { strokeDashoffset: '0' },
        },
      },
      animation: {
        floaty: 'floaty 5s ease-in-out infinite',
        fadeUp: 'fadeUp .9s ease both',
        marquee: 'marquee 28s linear infinite',
        dash: 'dash 2.8s linear infinite',
      },
    },
  },
};
