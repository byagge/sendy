const menuBtn = document.getElementById('menuBtn');
const mobileMenu = document.getElementById('mobileMenu');
const playDemo = document.getElementById('playDemo');
const demoModal = document.getElementById('demoModal');
const closeModal = document.getElementById('closeModal');
const phone = document.getElementById('phone');

menuBtn?.addEventListener('click', () => mobileMenu.classList.toggle('hidden'));

document.querySelectorAll('#mobileMenu a').forEach(link => {
  link.addEventListener('click', () => mobileMenu.classList.add('hidden'));
});

playDemo?.addEventListener('click', () => {
  demoModal.classList.remove('hidden');
  demoModal.classList.add('flex');
});

closeModal?.addEventListener('click', () => {
  demoModal.classList.add('hidden');
  demoModal.classList.remove('flex');
});

demoModal?.addEventListener('click', (e) => {
  if (e.target === demoModal) {
    demoModal.classList.add('hidden');
    demoModal.classList.remove('flex');
  }
});

window.addEventListener('keydown', (e) => {
  if (e.key === 'Escape') {
    demoModal.classList.add('hidden');
    demoModal.classList.remove('flex');
    mobileMenu.classList.add('hidden');
  }
});

document.querySelectorAll('.faq-item').forEach((item) => {
  const trigger = item.querySelector('.faq-trigger');
  const content = item.querySelector('.faq-content');
  const sign = trigger?.querySelector('span');

  trigger?.addEventListener('click', () => {
    const isOpen = !content.classList.contains('hidden');
    content.classList.toggle('hidden');
    if (sign) sign.textContent = isOpen ? '+' : '−';
  });
});

const revealObserver = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      entry.target.classList.add('is-visible');
      revealObserver.unobserve(entry.target);
    }
  });
}, { threshold: 0.2, rootMargin: '0px 0px -8% 0px' });

document.querySelectorAll('[data-reveal]').forEach((el) => {
  revealObserver.observe(el);
});

(() => {
  const liveChatDemo = document.getElementById('liveChatDemo');
  if (!liveChatDemo) return;

  const chatListEl    = document.getElementById('chatListItems');
  const chatMsgsEl    = document.getElementById('chatMessages');
  const typingEl      = document.getElementById('typingIndicator');
  const typingAvEl    = document.getElementById('typingAvatar');
  const headerAv      = document.getElementById('chatHeaderAvatar');
  const headerName    = document.getElementById('chatHeaderName');
  const headerSub     = document.getElementById('chatHeaderSub');
  const matchCardsEl  = document.getElementById('matchCards');
  const matchCardsMob = document.getElementById('matchCardsMob');
  const matchBadge    = document.getElementById('matchBadge');
  const matchBadgeMob = document.getElementById('matchBadgeMob');
  const mobileTabs    = document.getElementById('mobileTabs');
  const chatInput     = document.getElementById('chatInput');
  const chatSend      = document.getElementById('chatSend');

  const CHATS = [
    {
      id: 0, initials: 'DC', color: '#5B49F6', name: 'Дизайн-чат', sub: '23 участника · 10 в сети', online: true, preview: 'Ищу UX дизайнера...',
      msgs: [
        { av: 'JL', c: '#EC4899', n: 'Жасмин Л.', t: 'Всем привет! Кто занимается UI/UX для SaaS?', match: null },
        { av: 'AH', c: '#3B82F6', n: 'Алекс Х.',   t: 'Ищу UX дизайнера для fintech, бюджет обсуждается.', match: { phrase:'ищу дизайнера', flag:'fi-kz', region:'Казахстан', chat:'публичная группа', msg:'Ищу UX дизайнера для fintech, бюджет обсуждается.', time:'09:41' } },
        { av: 'OC', c: '#10B981', n: 'Осман Ч.',  t: 'Я работал с несколькими финтех стартапами, могу помочь.', match: null },
        { av: 'JC', c: '#F59E0B', n: 'Джейден Ч.', t: 'Кто может сделать редизайн мобильного приложения?', match: null },
      ]
    },
    {
      id: 1, initials: 'FG', color: '#3B82F6', name: 'Сообщество основателей', sub: '41 участник · 8 в сети', online: true, preview: 'Нужен маркетолог B2B',
      msgs: [
        { av: 'ZM', c: '#6366F1', n: 'Заид М.',   t: 'Есть кто из маркетологов в B2B?', match: null },
        { av: 'AC', c: '#F59E0B', n: 'Антон Ч.', t: 'Нужен маркетолог B2B, стартап серии A.', match: { phrase:'нужен маркетолог', flag:'fi-de', region:'Германия', chat:'Telegram-чат', msg:'Нужен маркетолог B2B, стартап серии A.', time:'09:43' } },
        { av: 'CG', c: '#EC4899', n: 'Коннор Г.',  t: 'Можно написать в личку, у меня есть контакты.', match: null },
      ]
    },
    {
      id: 2, initials: 'DH', color: '#10B981', name: 'Хаб разработчиков', sub: '89 участников · 22 в сети', online: false, preview: 'Ищу React-разработчика',
      msgs: [
        { av: 'VC', c: '#8B5CF6', n: 'Ванесса Ч.', t: 'Ищу React-разработчика на удалёнку, срочно.', match: { phrase:'ищу разработчика React', flag:'fi-us', region:'США', chat:'группа стартапов', msg:'Ищу React-разработчика на удалёнку, срочно.', time:'09:45' } },
        { av: 'JM', c: '#3B82F6', n: 'Яков М.',   t: 'Опыт с React 4 года, какой у вас стек?', match: null },
        { av: 'VC', c: '#8B5CF6', n: 'Ванесса Ч.', t: 'Next.js, TypeScript, Supabase — напишите в личку.', match: null },
      ]
    },
    {
      id: 3, initials: 'SK', color: '#F59E0B', name: 'Стартапы KZ', sub: '18 участников · 5 в сети', online: false, preview: 'Ищу CRM интегратора', badge: 3,
      msgs: [
        { av: 'NK', c: '#F59E0B', n: 'Nurgul K.',  t: 'Ищу CRM интегратора для Bitrix24, Алматы.', match: { phrase:'ищу CRM интегратора', flag:'fi-kz', region:'Казахстан', chat:'бизнес-чат', msg:'Ищу CRM интегратора для Bitrix24, Алматы.', time:'09:50' } },
        { av: 'BK', c: '#10B981', n: 'Bekzat K.',  t: 'У нас есть опыт с Bitrix в Казахстане, напиши.', match: null },
      ]
    },
  ];

  const KEYWORD_RULES = [
    { words: ['дизайнер', 'designer', 'ux', 'ui', 'figma', 'дизайн'],     label: 'дизайнер',    score: 96, flag: 'fi-kz', region: 'Казахстан' },
    { words: ['маркетолог', 'маркетинг', 'marketing', 'smm', 'таргет'],   label: 'маркетолог',  score: 88, flag: 'fi-de', region: 'Германия' },
    { words: ['разработчик', 'developer', 'react', 'backend', 'frontend'], label: 'разработчик', score: 92, flag: 'fi-us', region: 'США' },
    { words: ['юрист', 'адвокат', 'lawyer', 'договор', 'legal'],          label: 'юрист',        score: 81, flag: 'fi-ru', region: 'Россия' },
    { words: ['квартира', 'аренда', 'сниму', 'недвижимость', 'rent'],     label: 'квартира',     score: 84, flag: 'fi-kz', region: 'Казахстан' },
    { words: ['crm', 'интегратор', 'битрикс', 'bitrix', 'amocRM'],        label: 'CRM интегратор', score: 79, flag: 'fi-kz', region: 'Казахстан' },
  ];
  const KEYWORDS = ['ищу', 'нужен', 'нужна', 'looking for', 'wanted', 'search', 'требуется', 'find', 'хочу', 'подберите'];

  let matchCount = 0;

  const addMatchCard = (m) => {
    matchCount++;
    matchBadge.textContent = matchCount;
    if (matchBadgeMob) matchBadgeMob.textContent = matchCount;
    const chatLabel = m.chat || m.src || '';
    const msgText = m.msg || '';
    const card = document.createElement('article');
    card.className = 'relative glass rounded-[14px] p-4 shadow-card';
    card.style.cssText = 'opacity:0;transform:translateY(10px);transition:opacity .55s ease,transform .55s ease';
    card.innerHTML = `
          <div class="flex items-center justify-between">
            <div class="flex items-center gap-[5px] text-[12px] font-extrabold text-violet"><span>🔥</span> Новое совпадение</div>
            <div class="text-[11px] text-[#8A90A2]">${m.time}</div>
          </div>
          <div class="mt-2 space-y-1 text-[11.5px] leading-[1.4] text-[#141926]">
            <p><b>Фраза:</b> ${m.phrase}</p>
            <p><b>Регион:</b> <span class="fi ${m.flag} mr-1"></span>${m.region}</p>
            ${msgText ? `<p><b>Сообщение:</b> ${msgText}</p>` : ''}
            <p class="text-[#737A8D]"><b class="text-[#555C70]">Чат:</b> ${chatLabel}</p>
          </div>
          <div class="mt-3 grid grid-cols-2 gap-2">
            <button type="button" class="rounded-[10px] border border-[#E2E5F0] bg-white py-2 text-[11px] font-semibold text-[#374151]">Автор</button>
            <button type="button" class="rounded-[10px] bg-violet py-2 text-[11px] font-semibold text-white">Открыть чат</button>
          </div>`;
    matchCardsEl.prepend(card);
    requestAnimationFrame(() => { card.style.opacity = '1'; card.style.transform = 'translateY(0)'; });
    if (matchCardsMob) {
      const card2 = card.cloneNode(true);
      card2.style.cssText = 'opacity:0;transform:translateY(8px);transition:opacity .5s ease,transform .5s ease';
      matchCardsMob.prepend(card2);
      requestAnimationFrame(() => { card2.style.opacity = '1'; card2.style.transform = 'translateY(0)'; });
    }
  };

  const addMsg = (item, cb) => {
    const wrap = document.createElement('div');
    wrap.className = 'flex items-end gap-2';
    wrap.style.cssText = 'opacity:0;transform:translateY(8px);transition:opacity .5s ease,transform .5s ease';
    wrap.innerHTML = `
          <div class="grid h-7 w-7 shrink-0 place-items-center rounded-full text-[10px] font-bold text-white" style="background:${item.c}">${item.av}</div>
          <div class="max-w-[75%]">
            <p class="mb-0.5 text-[10px] text-[#A0A5B4]">${item.n}</p>
            <div class="rounded-[14px] bg-white px-3 py-2 shadow-[0_4px_14px_rgba(30,39,68,.07)]">
              <p class="text-[12.5px] text-[#20283B]">${item.t}</p>
            </div>
          </div>`;
    chatMsgsEl.appendChild(wrap);
    requestAnimationFrame(() => { wrap.style.opacity = '1'; wrap.style.transform = 'translateY(0)'; });
    chatMsgsEl.scrollTo({ top: chatMsgsEl.scrollHeight, behavior: 'smooth' });
    if (cb) setTimeout(cb, 0);
  };

  const addUserMsg = (text) => {
    const wrap = document.createElement('div');
    wrap.className = 'flex justify-end';
    wrap.style.cssText = 'opacity:0;transform:translateY(8px);transition:opacity .45s ease,transform .45s ease';
    wrap.innerHTML = `<div class="max-w-[74%] rounded-[14px] bg-[#5B49F6] px-3 py-2 text-white shadow-[0_6px_18px_rgba(91,73,246,.28)]"><p class="text-[12.5px]">${text}</p></div>`;
    chatMsgsEl.appendChild(wrap);
    requestAnimationFrame(() => { wrap.style.opacity = '1'; wrap.style.transform = 'translateY(0)'; });
    chatMsgsEl.scrollTo({ top: chatMsgsEl.scrollHeight, behavior: 'smooth' });
  };

  const showTyping = (av, c) => {
    typingAvEl.textContent = av;
    typingAvEl.style.background = c;
    typingEl.classList.remove('hidden');
    typingEl.classList.add('flex');
  };
  const hideTyping = () => { typingEl.classList.add('hidden'); typingEl.classList.remove('flex'); };

  let activeChat = -1;
  let animTimer = null;

  const loadChat = (idx) => {
    if (activeChat === idx) return;
    activeChat = idx;
    if (animTimer) clearTimeout(animTimer);
    chatMsgsEl.innerHTML = '';
    hideTyping();

    const chat = CHATS[idx];
    headerAv.textContent = chat.initials;
    headerAv.style.background = chat.color;
    headerName.textContent = chat.name;
    headerSub.textContent = chat.sub;

    document.querySelectorAll('.chat-list-row').forEach((r, i) => {
      r.classList.toggle('bg-[#F4F3FF]', i === idx);
    });
    document.querySelectorAll('.mobile-tab').forEach((t, i) => {
      t.classList.toggle('bg-violet', i === idx);
      t.classList.toggle('text-white', i === idx);
      t.classList.toggle('border-violet', i === idx);
      t.classList.toggle('bg-white', i !== idx);
      t.classList.toggle('text-[#4A5268]', i !== idx);
      t.classList.toggle('border-[#E2E5F0]', i !== idx);
    });

    let delay = 300;
    chat.msgs.forEach((msg) => {
      const td = delay;
      animTimer = setTimeout(() => {
        showTyping(msg.av, msg.c);
        animTimer = setTimeout(() => {
          hideTyping();
          addMsg(msg, null);
          if (msg.match) setTimeout(() => addMatchCard(msg.match), 600);
        }, 900);
      }, td);
      delay += 1800;
    });
  };

  const buildList = () => {
    chatListEl.innerHTML = '';
    if (mobileTabs) mobileTabs.innerHTML = '';
    CHATS.forEach((chat, idx) => {
      const row = document.createElement('div');
      row.className = `chat-list-row flex cursor-pointer items-center gap-3 px-4 py-3 transition hover:bg-[#F4F3FF] ${idx === 0 ? 'bg-[#F4F3FF]' : ''}`;
      row.innerHTML = `
            <div class="relative shrink-0">
              <div class="grid h-10 w-10 place-items-center rounded-full text-[13px] font-bold text-white" style="background:${chat.color}">${chat.initials}</div>
              ${chat.online ? '<span class="absolute -bottom-0.5 -right-0.5 h-3 w-3 rounded-full border-2 border-white bg-emerald-400"></span>' : ''}
            </div>
            <div class="min-w-0 flex-1">
              <div class="flex items-center justify-between">
                <p class="text-[13px] font-semibold text-[#1E2537]">${chat.name}</p>
                ${chat.badge ? `<span class="grid h-4 w-4 place-items-center rounded-full bg-violet text-[10px] font-bold text-white">${chat.badge}</span>` : ''}
              </div>
              <p class="truncate text-[12px] text-[#7D8396]">${chat.preview}</p>
            </div>`;
      row.addEventListener('click', () => loadChat(idx));
      chatListEl.appendChild(row);

      if (mobileTabs) {
        const tab = document.createElement('button');
        tab.className = `mobile-tab shrink-0 flex items-center gap-1.5 rounded-full border px-3 py-1 text-[12px] font-semibold transition ${idx === 0 ? 'border-violet bg-violet text-white' : 'border-[#E2E5F0] bg-white text-[#4A5268]'}`;
        tab.innerHTML = `<span class="grid h-5 w-5 place-items-center rounded-full text-[9px] font-bold text-white" style="background:${chat.color}">${chat.initials}</span>${chat.name}`;
        tab.addEventListener('click', () => loadChat(idx));
        mobileTabs.appendChild(tab);
      }
    });
  };

  const addUserMatchCard = (val, rule) => {
    const now = new Date();
    const time = `${String(now.getHours()).padStart(2,'0')}:${String(now.getMinutes()).padStart(2,'0')}`;
    matchCount++;
    matchBadge.textContent = matchCount;
    const card = document.createElement('article');
    card.className = 'relative glass rounded-[14px] p-4 shadow-card ring-1 ring-violet/20';
    card.style.cssText = 'opacity:0;transform:translateY(10px);transition:opacity .55s ease,transform .55s ease';
    card.innerHTML = `
          <div class="flex items-center justify-between">
            <div class="flex items-center gap-[5px] text-[12px] font-extrabold text-violet"><span>🔥</span> Новое совпадение</div>
            <div class="text-[11px] text-[#8A90A2]">${time}</div>
          </div>
          <div class="mt-2 space-y-1 text-[11.5px] leading-[1.4] text-[#141926]">
            <p><b>Фраза:</b> ${rule ? rule.label : val.slice(0, 28)}</p>
            <p><b>Регион:</b> <span class="fi ${rule ? rule.flag : 'fi-kz'} mr-1"></span>${rule ? rule.region : 'Казахстан'}</p>
            <p><b>Сообщение:</b> ${val.slice(0, 120)}${val.length > 120 ? '…' : ''}</p>
            <p class="text-[#737A8D]"><b class="text-[#555C70]">Чат:</b> этот чат</p>
          </div>
          <div class="mt-3 grid grid-cols-2 gap-2">
            <button type="button" class="rounded-[10px] border border-[#E2E5F0] bg-white py-2 text-[11px] font-semibold text-[#374151]">Автор</button>
            <button type="button" class="rounded-[10px] bg-violet py-2 text-[11px] font-semibold text-white">Открыть чат</button>
          </div>`;
    matchCardsEl.prepend(card);
    requestAnimationFrame(() => { card.style.opacity = '1'; card.style.transform = 'translateY(0)'; });
  };

  const sendUserMsg = () => {
    const val = chatInput.value.trim();
    if (!val) return;
    addUserMsg(val);
    chatInput.value = '';
    const low = val.toLowerCase();
    const hasIntent = KEYWORDS.some(k => low.includes(k));
    const matchedRule = KEYWORD_RULES.find(r => r.words.some(w => low.includes(w)));
    if (hasIntent || matchedRule) {
      setTimeout(() => addUserMatchCard(val, matchedRule || null), 1100);
    }
  };

  chatSend?.addEventListener('click', sendUserMsg);
  chatInput?.addEventListener('keydown', (e) => { if (e.key === 'Enter') sendUserMsg(); });

  buildList();

  const chatObserver = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) { loadChat(0); chatObserver.disconnect(); }
    });
  }, { threshold: 0.25 });
  chatObserver.observe(liveChatDemo);
})();

document.addEventListener('mousemove', (e) => {
  if (!phone || window.innerWidth < 1024) return;
  const rect = phone.getBoundingClientRect();
  const cx = rect.left + rect.width / 2;
  const cy = rect.top + rect.height / 2;
  const dx = (e.clientX - cx) / rect.width;
  const dy = (e.clientY - cy) / rect.height;
  phone.style.transform = `perspective(900px) rotateY(${dx * 3}deg) rotateX(${-dy * 3}deg)`;
});

document.addEventListener('mouseleave', () => {
  if (phone) phone.style.transform = 'perspective(900px) rotateY(0) rotateX(0)';
});
