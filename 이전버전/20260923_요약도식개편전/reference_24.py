# -*- coding: utf-8 -*-
OLD_SLIDES=S[:];S=[]
def keep(old,cat=None,title=None,sub=None,body=None,cls=''):
 r=OLD_SLIDES[old-1].copy();r['no']=len(S)+1
 if cat:r['cat']=cat
 if title:r['title']=title
 if sub is not None:r['sub']=sub
 if body is not None:
  r['notes']+='\n발표 참고(이전 상세 설명): '+re.sub('<[^>]*>',' ',r['body'])
  r['body']=body
 r['cls']=cls;S.append(r)
def panel(k,t,p=''):return card(k,t,p)
def fig(name,caption):return photo(name,caption)
# Reference order: cover, contents, summary, market/problem 4, solution 2,
# traction 2, expansion 2, revenue, competition 4, mission/funds 2, team, close, appendix2.
keep(1,cat='사업소개서',sub='10–15세 전문 · 주니어골든에이지',cls='cover')
toc=[('목차','01'),('요약','02'),('시장 현황 및 문제','03–06'),('해결 방법','07–08'),('성과 (요약 및 상세)','09–10'),('확장 전략','11–12'),('향후 매출 목표','13'),('경쟁사 분석','14–17'),('미션 / 투자금 사용계획','18–19'),('팀원 소개','20'),('마무리','21'),('Appendix','22–23')]
keep(2,cat='목차',title='목차',sub='',body='<div class="reference-toc">'+''.join(f'<div><span>{i+1}. {a}</span><i></i><b>{n}</b></div>' for i,(a,n) in enumerate(toc))+'</div>')
keep(2,cat='요약',title='전체 사업소개서 요약',sub='바이오밴딩 기반 · 유소년 종합성장관리',body='<div class="summary-layout"><div class="summary-list">'+''.join(f'<div><b>{i+1:02}</b><span>{t}</span></div>' for i,t in enumerate(['10–15세 성장기 선수에 집중','성장·피지컬·멘탈을 하나의 기준으로','측정 → 강화 → 재측정의 반복 관리','서울 R&D 센터 → 의료·피지컬 제휴망','본사 전문인력·제품·운영에 투자']))+'</div><div>'+fig('추가PPT/image20.jpeg','선수와 부모를 만나는 현장')+stat('240억','5년차 매출 시나리오','239.972억 · 실적 아닌 계획')+'</div></div>')
keep(4,cat='시장 현황 및 문제',title='실력을 펼치기도 전에,<br><em>재능이 낙오됩니다</em>',sub='중학교 진입기 · 실력 외 부담이 겹치는 과정',body='<div class="dropout-short"><div>'+fig('추가PPT/image21.jpeg','측정과 상담이 필요한 성장기')+flow([('성장 격차','체격·성숙도'),('부담 누적','통증·비교 압박'),('참여 위축','자신감·훈련 공백'),('중단 위험','재미·소속감 약화')])+'</div><aside><small>초기 장표 인용</small><strong>43%+</strong><h3>중학교 전후 탈락률로 제시</h3><p>원통계·모집단·산식<br><b>재확인 필요</b></p><small>실력 외 사유의 비율로<br>확인된 수치는 아닙니다.</small></aside></div>')
keep(13,cat='시장 현황',title='측정에서 종합관리로,<br><em>확장 기회 1.2조 원</em>',sub='대상 인원 × 연간 지출 · 검증 전 시장 시나리오',body='<div class="market-keywords">'+grid(stat('720억','축구 선수','2만 명 × 연360만'),stat('1,800억','타 종목 선수','5만 명 × 연360만'),stat('1.2조','활동 아동 확장','50만 명 × 연240만'))+hbars(['낮은 범위','중앙 범위','높은 범위'],[.3,1.2,2.7],'조',3)+'</div>')
keep(4,cat='문제',title='부모도 지도자도,<br><em>판단할 근거가 필요합니다</em>',sub='불안을 성장·피지컬·멘탈의 지원으로',body=table(['영역','부모의 불안','지도자의 불안'],[['S · 성장','왜 우리 아이만 작을까?','기다릴까, 지금 평가할까?'],['P · 피지컬','아픈데 계속 뛰어도 될까?','훈련을 늘릴까, 쉬게 할까?'],['M · 멘탈','자신감을 잃으면 어쩌지?','의욕 저하일까, 도움이 필요할까?']])+band('성장단계 해석 → 컨디셔닝 → 멘탈 지원'),cls='big-table')
keep(5,cat='문제 · 해외 선행 사례',title='같은 나이,<br><em>다른 성장의 시간</em>',sub='해외 바이오밴딩에서 시작된 문제의식',body='<div class="maturity-layout"><div class="maturity-bands"><span>역연령</span><div><b>12세</b><b>12세</b><b>12세</b></div><span>성숙도</span><div><i>성장 이전</i><i>가속기</i><i>급성장기</i></div></div><div>'+art()+'</div></div>'+band('현재 체격에 가려진 <b>성장의 맥락</b>을 함께 봅니다.'),cls='maturity-slide')
keep(7,cat='해결 방법',title='측정 결과를,<br><em>다음 행동으로 연결합니다</em>',sub='실제 제작 리포트 · 가상 선수·예시 데이터',body='<div class="solution-reports"><figure><button class="zoom">'+pic(A/'mental-3.png','멘탈 리포트 샘플')+'</button><figcaption>M · 성장단계 × 마음</figcaption></figure><figure><button class="zoom">'+pic(A/'physical-2.png','피지컬 리포트 샘플')+'</button><figcaption>P · 몸 상태 × 성장단계</figcaption></figure><div>'+flow([('측정','M · P · S'),('해석','지원 우선순위'),('강화','실천·재측정')])+'<p class="large-key">점수 다음에,<br><em>관리와 연습.</em></p></div></div>')
S[-1]['source']='첨부 최신 멘탈PDF p.3 · 피지컬PDF p.2 | 가상 샘플·내부 기준. 효과·진단 정확도 입증 아님.'
keep(9,cat='해결 방법',title='세 가지 강화,<br><em>하나의 선수 기록</em>',sub='',body='<div class="service-tiles">'+''.join('<article>'+fig(n,c)+f'<small>{k}</small><h2>{t}</h2><p>{p}</p></article>' for n,c,k,t,p in [('growth-01.jpg','성장 측정 현장','S · 성장','의료기관 연계','측정 → 상담·진료 → 경과'),('추가PPT/image22.jpeg','신체 측정 현장','P · 피지컬','MPS 스튜디오','측정 → 컨디셔닝 → 재측정'),('추가PPT/image21.jpeg','멘탈 현장 운영','M · 멘탈','본사 심리상담','측정 → 멘토링 → 리뷰')])+'</div>')
keep(11,cat='성과',title='현장 기록과 수요 신호,<br><em>제품으로 이어집니다</em>',sub='내부 집계 · 설문과 구매 실적 구분',body='<div class="traction-key"><div>'+donut([83.1,16.9],['검사 의향 (%)','그 외 (%)'],'83.1%','부모325명 설문')+grid(stat('950+','측정·평가 기록','유료 고객 수 아님'),stat('40여 팀','네트워크 표기','유료 계약 수 아님'),cols=2)+'</div>'+fig('추가PPT/image20.jpeg','기존 팀·선수 현장 접점')+'</div>')
keep(23,cat='성과 · 실행 인력',title='현장을 해본 전문가가,<br><em>결과를 실행으로</em>',sub='의료 · 스포츠 · 심리 · 기술의 연결',body='<div class="expert-evidence"><div>'+fig('추가PPT/teamdoctor.jpg','전문가 워크숍 · 기존 사업자료')+'</div><div>'+grid(panel('대표 / 팀닥터','이정욱','20년 임상·운영 경험'),panel('현장 / 스포츠','김학인','축구행정·스포츠마케팅'),panel('멘탈 / 고객 경험','황원','선수 출신·심리상담'),panel('제품 / 개발','이준우','AI 웹솔루션 개발'),cols=2)+'</div></div>')
keep(16,cat='확장 전략',title='서울 R&D 센터에서,<br><em>반복 관리 모델을 검증합니다</em>',sub='측정은 본사팀 지원 · 현장은 컨디셔닝과 회원 운영',body='<div class="center-reference">'+fig('sdr1.jpg','현재 센터 사진 · 신규 플래그십 완공 사진 아님')+'<div>'+grid(stat('120명','활성회원','월40만 원 환산'),stat('40명','월 별도 측정','단회12만 원 가정'),cols=2)+flow([('가입','측정·설명'),('관리','회차권·강화'),('유지','리뷰·재측정')])+band('측정 → 관리 → 멤버십')+'</div></div>')
keep(19,cat='확장 전략',title='한의원·피지컬센터로,<br><em>플랫폼 계약을 확장합니다</em>',sub='2031 한의원100곳 + 피지컬100곳 · 가동85% 가정',body='<div class="network-reference"><div>'+grid(panel('인증 한의원','월80만','SaaS50 + 인증·운영30'),panel('피지컬센터','월50만','SaaS30 + 운영지원20'),cols=2)+band('공동광고 · 월20만 /10만 별도<br><span>초기 가맹비 미정 · 광고 수납은 매출 합계 제외</span>')+'</div><div>'+donut([8.16,5.1],['한의원 (억)','피지컬 (억)'],'13.26억','연 계약매출 가정')+'</div></div>')
keep(20,cat='향후 매출 목표',title='5년차,<br><em>240억 원 매출 시나리오</em>',sub='계획·가정 / 실제 매출 추세 아님',body='<div class="revenue-reference"><div>'+linechart([str(r['year']) for r in model],[r['total_krw']/1e8 for r in model],'회사 귀속 매출 계획 · 억 원')+'</div><div class="unit-summary"><small>서울 R&D 센터 · 월 검증 모델</small>'+table(['매출 /비용','만원'],[['회원120명 ×40만','4,800'],['측정40명 ×12만 /팀계약','480 /125'],['인건비 /임차 /기타','600 /600 /500'],['변동비10%','540.5'],['운영 잉여 · 본사배부 전','3,164.5']])+'<p>월매출 <b>5,405만</b> · 연매출 <b>6.486억</b></p></div></div>')
S[-1]['source']+=' | 센터 인건비600만(대표 지시), 임차600·기타500·변동10% 기존 가정. 본사공용비·감가·세금 전.'
keep(21,cat='경쟁사 분석',title='MPS의 포지션은,<br><em>성장단계 × 통합 지원</em>',sub='서비스 역할의 개념도 · 기능 우열·점유율 도표 아님',body='<div class="position-map"><div class="axis-y">성장단계 해석 ↑</div><div class="axis-x">지속적인 통합 지원 →</div><span class="pos-med">성장 평가·진료</span><span class="pos-fit">체력 측정</span><span class="pos-train">훈련·컨디셔닝</span><span class="pos-mps">MPS<small>지향 포지션</small></span></div>')
keep(21,cat='경쟁사 분석 · 국내',title='국내 서비스와,<br><em>MPS의 집중 영역</em>',sub='공개된 기능을 공정하게 비교합니다.',body=table(['구분','PLCO · 공개 서비스','MPS · 개발·운영 방향'],[['대상','유소년·엘리트 팀','10–15세 성장기 선수'],['측정·현장','피지컬 측정·리포트·훈련','성장단계 × M·P·S 통합 해석'],['연결','앱·웹·오프라인 짐','의료기관·본사 멘탈·스튜디오'],['입증할 차이','공식 제공 범위 확인','구매 이유·유지율·관리 완료율']]),cls='big-table')
keep(22,cat='경쟁사 분석 · 해외',title='해외 사례에서,<br><em>육성과 사업모델을 배웁니다</em>',sub='적용 방향 · 동일 서비스·성과·제휴를 의미하지 않음',body=grid(panel('ENGLAND','Premier League','성숙도 기반 경기 운영'),panel('JAPAN · LAB','ARROWZ LAB','스포츠과학 측정·평가'),panel('JAPAN · GYM','ARROWZ GYM','훈련·재측정·앱 기록'))+flow([('교류','운영·연구'),('현지화','기준·언어'),('파일럿','수요·재현성'),('진출','파트너 계약')]))
S[-1]['source']+=' · '+link(ARG,'ARROWZ GYM 공식 안내')
keep(22,cat='경쟁사 분석 · 사례',title='LAB에서 GYM으로,<br><em>측정이 반복 관리로 이어집니다</em>',sub='ARROWZ 모델 참고 → MPS 운영에 적용할 구조',body='<div class="case-reference"><div><small>ARROWZ · 공개 운영</small>'+flow([('연간','스포츠독'),('매월','필드 테스트'),('매주','훈련')])+'<h2>측정 + 훈련 + 앱</h2></div><div><small>MPS · 실행 방향</small>'+flow([('측정','M·P·S'),('관리','전문가 강화'),('재측정','다음 계획')])+'<h2><em>성장단계 + 통합 지원</em></h2></div></div>')
S[-1]['source']=link(ARG,'ARROWZ 공식: 연간 측정·월간 테스트·주간 훈련·앱')+' | MPS 연결 구조는 실행 계획. 해외 매출은 재무 모델 미포함.'
keep(29,cat='미션',title='지도자는 축구에,<br><em>MPS는 선수의 성장에</em>',sub='멘탈성향·부상·성장차이로 재능이 낙오되지 않도록',body='<div class="mission-reference"><div>'+art()+'</div><div><h2>서울에서 증명하고,<br>전국의 성장관리로.</h2><p>의료기관 · 스튜디오 · 본사 멘탈</p><div class="mission-sign">주니어골든에이지<br><b>대표 이정욱</b></div></div></div>',cls='mission-slide')
keep(26,cat='투자금 사용계획',title='성장을 위한 투자',sub='20억 원 · 18개월 실행 검토안 / 라운드 금액·조건 미확정',body='<div class="fund-reference"><div>'+donut([6,5,4,2,1,1,1],['전문인력 (억)','센터','플랫폼','데이터','해외','마케팅','예비'],'20억','검토안')+'</div><div class="fund-priorities">'+panel('01','R&D·전문인력','검증 기준 · 실행 조직')+panel('02','플랫폼·프로그램','앱 · 리포트 · 강화 서비스')+panel('03','서울 센터·네트워크','직영 검증 · 제휴 · 해외교류')+'</div></div>')
keep(24,cat='팀원 소개',title='현장 경험과 실행력이 강점인 팀',sub='대표의 임상·팀닥터·부모 경험을 제품과 현장 운영으로',cls='team-reference')
# Shorten team text; preserve requested placement.
S[-1]['body']=S[-1]['body'].replace('AI 웹솔루션 개발 총괄<br>무신사·카카오 서비스 연계 경력','AI 웹솔루션 개발').replace('한의학박사·전문의 / 소아과 교수','한의학박사·전문의')
keep(18,cat='마무리',title='11명의 선수,<br><em>11가지 성장의 시간</em>',sub='측정으로 이해하고, 함께 관리합니다.',body='<div class="closing-reference"><div><h2>아이의 지금이<br>미래를 닫지 않도록.</h2><p>부모에게는 근거를.<br>지도자에게는 지원을.<br>선수에게는 성장의 시간을.</p></div><div class="cycle"><div>측정<br><b>M·P·S</b></div><div>해석<br><b>전문가</b></div><div>강화<br><b>개별 지원</b></div><div>재측정<br><b>다음 계획</b></div><span>MPS</span></div></div>')
logo_names=['image18.jpeg','image14.jpeg','image15.jpeg','image19.jpeg','image12.jpeg','image7.jpeg','image13.jpeg','image39.png','image38.png','image10.jpeg','image8.jpeg','image9.jpeg','image11.jpeg','image42.png','image16.jpeg','image41.png','image40.png','image17.jpeg']
keep(11,cat='Appendix · 네트워크',title='축구 현장에서 쌓은,<br><em>첫 고객 접점</em>',sub='기존 사업자료에 수록된 팀·기관 네트워크',body='<div class="network-logos">'+''.join(pic(PH/'추가PPT'/n,'기존 자료 수록 팀 엠블럼') for n in logo_names)+'</div>'+band('<b>40여 팀</b> · 현장 접점과 협력 파이프라인'))
S[-1]['source']='기존 사업제안서 사진자료/추가PPT 엠블럼 · 내부 네트워크 표기 | 현재 유료계약·독점·기관 보증을 의미하지 않음.'
keep(11,cat='Appendix · 현장',title='선수가 있는 곳에서,<br><em>측정의 경험을 만듭니다</em>',sub='',body='<div class="field-gallery">'+fig('추가PPT/image20.jpeg','팀과 함께 · 부모·선수 접점')+fig('growth-01.jpg','측정 현장 · 성장 평가')+fig('추가PPT/image23.jpeg','워크숍 · 전문가 해석')+'</div>')
S[-1]['source']='사업제안서 사진자료: image20.jpeg · growth-01.jpg · image23.jpeg | 실제 과거 현장 사진; 전원 유료 고객·신규 계약을 뜻하지 않음.'
assert len(S)==24
# Final presentation copy: single-line headings and concise status labels.
titles=[
 '바이오밴딩 기반 유소년 축구선수 <em>종합성장관리 플랫폼</em>',
 '목차','전체 사업소개서 요약',
 '실력을 펼치기 전, <em>재능이 낙오됩니다</em>',
 '종합성장관리로 <em>1.2조 원의 확장 기회</em>',
 '부모와 지도자에게 <em>판단의 근거를</em>',
 '같은 나이, <em>다른 성장의 시간</em>',
 '측정 결과를 <em>다음 행동으로</em>',
 '세 가지 강화, <em>하나의 선수 기록</em>',
 '현장의 기록과 수요를 <em>제품으로</em>',
 '현장을 해본 전문가의 <em>실행력</em>',
 '서울 R&D 센터에서 <em>반복 관리 모델 검증</em>',
 '의료·피지컬 제휴 네트워크로 <em>플랫폼 확장</em>',
 '5년차 <em>240억 원 매출 시나리오</em>',
 'MPS의 포지션, <em>성장단계 × 통합 지원</em>',
 '국내 서비스와 <em>MPS의 집중 영역</em>',
 '해외 사례로 보는 <em>육성과 사업모델</em>',
 'LAB에서 GYM으로, <em>측정에서 반복 관리로</em>',
 '지도자는 축구에, <em>MPS는 선수의 성장에</em>',
 '성장을 위한 투자','현장 경험과 실행력이 강점인 팀',
 '11명의 선수, <em>11가지 성장의 시간</em>',
 '축구 현장에서 쌓은 <em>첫 고객 접점</em>',
 '선수가 있는 곳에서 <em>측정의 경험을</em>'
]
copy_edits={
 '의료·피지컬 제휴망':'의료·피지컬 제휴 네트워크',
 '239.972억 · 실적 아닌 계획':'239.972억 · 매출 시나리오',
 '실력 외 사유의 비율로<br>확인된 수치는 아닙니다.':'탈락 사유별 비중<br>추가 확인 필요',
 '유료 고객 수 아님':'누적 측정·평가 건수',
 '유료 계약 수 아님':'현장 접점·협력 기반',
 '현재 센터 사진 · 신규 플래그십 완공 사진 아님':'현재 운영 센터 · 서울 R&D 센터 구축 예정',
 '계획·가정 / 실제 매출 추세 아님':'2027–2031 매출 목표 · 계획 가정',
 '서비스 역할의 개념도 · 기능 우열·점유율 도표 아님':'성장단계 해석과 지속 관리의 연결 (예정)',
 '적용 방향 · 동일 서비스·성과·제휴를 의미하지 않음':'해외 모델 연구 · 교류·진출 (예정)',
 '도식은 가능한 경로이며 인과·비율 추정 아님. 학업·경제·진로 등 다른 이탈 요인도 존재.':'이탈 경로 개념도 · 학업·경제·진로 등 복합 요인.',
 '골연령은 심리적 나이가 아님; 임상·예측 정확도 검증 진행 전':'골연령: 신체 성숙도 지표 · 임상·예측 정확도 검증 예정',
 '가상 샘플·내부 기준. 효과·진단 정확도 입증 아님.':'가상 샘플·내부 기준 · 효과·정확도 검증 예정',
 '누적 접점·선수·검사 건수의 정의가 달라 시계열 성장률로 합산하지 않음':'측정·평가 건수와 팀 접점을 각각 집계',
 'FIFA 축구의학 코스 수료(학위 아님).':'FIFA 축구의학 코스 수료.',
 '본사 인건비·공용원가 자체가 없어지는 것은 아님.':'본사 인건비·공용원가는 별도 관리.',
 '공개되지 않은 기능의 부재는 단정하지 않음':'공개된 서비스 범위 기준',
 '전 세계 보편적 상용화 주장 아님. 해외 제휴·진출은 계획, 체결 실적 아님':'해외 선행 사례 참고 · 해외 교류·제휴·진출 (예정)',
 '직책·경력은 내부자료 기준, 전원 상근 고용을 의미하지 않음. CTO 사진 미제공 상태.':'직책·경력은 내부자료 기준 · 상근·협력 인력 구성',
 '데이터 증가가 정확도 향상을 자동 보장하지 않음; 별도 검증 필요':'데이터 확충 · 정확도·재현성 검증 예정',
 '현재 유료계약·독점·기관 보증을 의미하지 않음.':'현장 접점·협력 네트워크 기준.',
 '실제 과거 현장 사진; 전원 유료 고객·신규 계약을 뜻하지 않음.':'실제 측정·교류 현장 기록.',
}
for r,t in zip(S,titles):
 r['title']=t
 r['notes']+='\n문구 정리 전 참고: '+r['sub']+' '+r['source']
 for key in ('sub','body','source'):
  for before,after in copy_edits.items():r[key]=r[key].replace(before,after)
old_photo=fig('추가PPT/image20.jpeg','선수와 부모를 만나는 현장')
new_photo='<figure class="warm-photo">'+pic(A/'tournament-mps.jpeg','2026 청춘양구 축구페스티벌 MPS 측정 현장')+'<figcaption>선수와 부모, 팀을 만나는 대회 현장</figcaption></figure>'
assert old_photo in S[2]['body']
S[2]['body']=S[2]['body'].replace(old_photo,new_photo)
S[2]['source']+=' · 사진: 2026 청춘양구 축구페스티벌 MPS 측정 현장'
REFERENCE_CSS='''
:root{--ink:#202126;--muted:#67686f;--orange:#fc582b;--purple:#8874b8;--cream:#fff}body{background:#e9e9ec}.slide{background:#fff}.slide:before{display:none}.card,.stat,.flow article{background:#f6f6f8;border:0}.peach,.band{background:#fff0e6}.lavender{background:#f0edf7}.card,.stat{border-radius:18px}th{background:#24252a}td{border-color:#dedee3}tbody tr:nth-child(even){background:#f7f7f9}footer{border-color:#dddde1}footer .source{color:#73737a}.warm-photo{background:#fafafa;border:1px solid #e7e7eb;border-radius:15px}.warm-photo figcaption{color:#74747b;font-size:16px;text-align:center;padding:14px}.warm-photo img{height:300px;object-position:center;object-fit:cover}.content{top:268px;bottom:116px}.card h3{font-size:31px}.card p{font-size:23px}.card small{font-size:15px}.band{font-size:25px}.flow h3{font-size:28px}.flow p{font-size:20px}.stat strong{font-size:59px}.stat h3{font-size:26px}.stat p{font-size:18px}.heading h1{font-size:48px}.subtitle{font-size:20px}.reference-toc{display:grid;gap:13px;padding:0 50px;max-width:1350px}.reference-toc>div{display:flex;align-items:center;gap:24px;font-size:24px}.reference-toc i{flex:1;border-bottom:1px dotted #d8d8dd}.reference-toc b{font-size:20px;width:85px;text-align:right}.summary-layout{display:grid;grid-template-columns:1.2fr .8fr;gap:48px}.summary-list{display:grid;gap:25px;padding-top:15px}.summary-list>div{display:flex;gap:25px;font-size:29px;line-height:1.5}.summary-list b{color:#fc582b}.summary-layout .warm-photo img{height:255px}.summary-layout .stat{margin-top:19px;padding:16px 25px}.summary-layout .stat strong{font-size:40px}.summary-layout .stat h3{display:inline;font-size:23px;margin-left:20px}.summary-layout .stat p{font-size:16px;margin-top:7px}.dropout-short{display:grid;grid-template-columns:1fr 340px;gap:30px}.dropout-short .warm-photo{width:560px;margin:0 auto 22px}.dropout-short .warm-photo img{height:255px}.dropout-short .flow article{padding:15px}.dropout-short .flow h3{font-size:23px}.dropout-short .flow p{font-size:16px}.dropout-short aside{background:#fff1e8;border-radius:20px;padding:28px}.dropout-short aside>strong{font-size:70px;color:#fc582b;display:block;margin:15px 0}.dropout-short aside h3{font-size:27px;line-height:1.5}.dropout-short aside p{font-size:19px;margin:24px 0;background:#fff;padding:16px}.dropout-short aside small{font-size:16px;line-height:1.7;color:#796a62}.market-keywords .warm-bars{max-width:950px;margin:0 auto;padding:15px 0}.big-table table{font-size:27px}.big-table th{font-size:21px;padding:21px}.big-table td{padding:28px 20px}.maturity-layout{display:grid;grid-template-columns:1fr 450px;gap:40px;height:345px}.maturity-bands{padding:10px 30px}.maturity-bands>span{display:block;font-size:20px;color:#73737b;margin-bottom:14px}.maturity-bands>div{display:flex;gap:25px;margin-bottom:30px}.maturity-bands b,.maturity-bands i{flex:1;text-align:center;font-style:normal;padding:25px 15px;background:#f5f5f7;border-radius:18px;font-size:32px}.maturity-bands i{font-size:27px;background:#eee9f5}.maturity-bands i:nth-child(2){background:#f7e4d8}.maturity-bands i:nth-child(3){background:#e9efdf}.maturity-slide .hero-boy{top:0;right:0;height:340px;width:360px}.maturity-slide .band{margin-top:25px}.solution-reports{display:grid;grid-template-columns:360px 360px 1fr;gap:35px}.solution-reports figure{text-align:center}.solution-reports .zoom{height:440px}.solution-reports figcaption{font-size:22px;margin-top:13px}.solution-reports .flow{grid-auto-flow:row;gap:12px}.solution-reports .flow article{padding:15px 23px}.solution-reports .flow article:after{display:none}.solution-reports .flow h3{display:inline;font-size:26px;margin:0 15px}.solution-reports .flow p{display:inline;font-size:21px}.large-key{font-size:43px;line-height:1.5;font-weight:700;margin-top:32px}.service-tiles{display:grid;grid-template-columns:repeat(3,1fr);gap:30px}.service-tiles article{background:#f7f7f9;border-radius:20px;padding:20px}.service-tiles .warm-photo img{height:238px}.service-tiles .warm-photo figcaption{font-size:14px;padding:10px}.service-tiles small{display:block;color:#8874b8;font-size:17px;margin:20px 0 10px}.service-tiles h2{font-size:32px}.service-tiles p{font-size:21px;margin-top:14px}.traction-key{display:grid;grid-template-columns:1fr 600px;gap:35px}.traction-key .donut-layout{height:260px}.traction-key .warm-photo img{height:385px}.traction-key .stat{padding:20px}.traction-key .stat strong{font-size:45px}.traction-key .stat h3{font-size:23px}.expert-evidence{display:grid;grid-template-columns:610px 1fr;gap:35px}.expert-evidence .warm-photo img{height:370px;object-fit:contain}.expert-evidence .card{padding:25px}.expert-evidence .card h3{font-size:31px}.expert-evidence .card p{font-size:21px}.center-reference{display:grid;grid-template-columns:610px 1fr;gap:35px}.center-reference .warm-photo img{height:380px;object-fit:contain}.center-reference .flow{margin-top:25px}.center-reference .flow article{padding:16px}.center-reference .flow h3{font-size:25px}.center-reference .flow p{font-size:18px}.center-reference .stat{padding:22px}.center-reference .stat strong{font-size:47px}.center-reference .stat h3{font-size:23px}.center-reference .stat p{font-size:18px}.network-reference{display:grid;grid-template-columns:1fr 1fr;gap:35px;align-items:center}.network-reference .donut-layout{grid-template-columns:1fr;justify-items:center}.network-reference svg{height:290px}.network-reference .chart-legend{width:400px;font-size:19px}.network-reference .card p{font-size:20px}.network-reference .band{font-size:23px}.revenue-reference{display:grid;grid-template-columns:1.1fr 1fr;gap:35px}.revenue-reference .warm-line{height:430px}.unit-summary{background:#f7f7f9;border-radius:20px;padding:20px}.unit-summary>small{font-size:17px;display:block;margin-bottom:12px}.unit-summary table{font-size:18px}.unit-summary td{padding:15px}.unit-summary p{font-size:20px;margin-top:20px}.position-map{position:relative;margin:0 auto;width:1100px;height:455px;border-left:3px solid #c7c5cb;border-bottom:3px solid #c7c5cb;background:linear-gradient(90deg,transparent 49.8%,#eeeeef 50%,transparent 50.2%),linear-gradient(0deg,transparent 49.8%,#eeeeef 50%,transparent 50.2%)}.position-map>span{position:absolute;display:flex;align-items:center;justify-content:center;border-radius:50%;width:185px;height:135px;background:#f3f1f6;font-size:24px}.axis-y{position:absolute;top:0;left:15px;color:#777}.axis-x{position:absolute;bottom:-38px;right:0;color:#777}.pos-med{left:120px;top:75px}.pos-fit{left:120px;bottom:45px}.pos-train{right:130px;bottom:45px}.position-map .pos-mps{right:110px;top:45px;width:220px;height:155px;background:#fff0e6;color:#fc582b;font-size:42px;flex-direction:column;font-weight:800}.pos-mps small{font-size:17px;margin-top:12px}.case-reference{display:grid;grid-template-columns:1fr 1fr;gap:35px}.case-reference>div{padding:35px 25px;background:#f6f6f8;border-radius:20px}.case-reference small{font-size:18px;color:#777}.case-reference .flow{margin-top:30px}.case-reference .flow article{padding:16px;background:#fff}.case-reference .flow h3{font-size:24px}.case-reference .flow p{font-size:18px}.case-reference h2{font-size:32px;margin-top:30px}.mission-reference{display:grid;grid-template-columns:550px 1fr;gap:40px}.mission-reference>div:first-child{position:relative;height:470px}.mission-reference .hero-boy{inset:0;width:100%;height:100%}.mission-reference h2{font-size:54px;line-height:1.4;margin:50px 0 30px}.mission-reference p{font-size:25px}.mission-sign{font-size:21px;line-height:1.8;margin-top:40px}.fund-reference{display:grid;grid-template-columns:1.1fr 1fr;gap:40px}.fund-reference .donut-layout{height:450px}.fund-reference .chart-legend{font-size:19px}.fund-priorities{display:grid;gap:17px}.fund-priorities .card{padding:22px 27px}.fund-priorities .card small{margin-bottom:8px}.fund-priorities .card h3{font-size:29px;margin-bottom:9px}.fund-priorities .card p{font-size:21px}.team-main article,.team-support article{background:#f5f4f7}.team-reference .team-main p{font-size:19px}.team-reference .team-support .card p{font-size:15px}.closing-reference{display:grid;grid-template-columns:1fr 1fr;gap:40px}.closing-reference h2{font-size:50px;line-height:1.4;margin-top:35px}.closing-reference p{font-size:28px;line-height:1.8;margin-top:30px}.cycle{background:none}.cycle>div{background:#eee8f3}.network-logos{display:grid;grid-template-columns:repeat(6,1fr);gap:20px;max-width:1300px;margin:auto}.network-logos img{width:100%;height:105px;object-fit:contain}.field-gallery{display:grid;grid-template-columns:repeat(3,1fr);gap:28px}.field-gallery .warm-photo img{height:390px;object-fit:contain}.field-gallery .warm-photo figcaption{font-size:20px;padding:22px 12px}.chart-legend{color:#52525c}.warm-bars b{color:#656571}.warm-bars>div>div{background:#f0edf3}.warm-bars i{background:#e7b79a}.warm-bars>div:nth-child(2) i{background:#b6a3c4}.warm-bars>div:nth-child(3) i{background:#a7baa2}
'''
REFERENCE_CSS+='''
.heading h1{white-space:nowrap;line-height:1.25;font-size:46px}
.cover .heading{width:1480px;max-width:1480px}
.cover .heading h1{font-size:43px;letter-spacing:-1.5px}
.summary-list>div{font-size:26px;gap:20px}
.summary-layout .warm-photo img{height:310px;object-fit:contain}
.summary-layout .warm-photo figcaption{padding:11px;font-size:16px}
.summary-layout .stat{margin-top:14px;padding:12px 20px}
.summary-layout .stat strong{font-size:36px}
.summary-layout .stat h3{font-size:21px}
'''
# Cover identity and public-facing source labels.
S[0]['body']=re.sub(r'<div class="cover-tags">.*?</div>', '<div class="cover-tags"><span><b>M 멘탈</b> × 본사 상담</span><span><b>P 피지컬</b> × 스튜디오</span><span><b>S 성장 측정</b> × 의료기관</span></div><div class="cover-presenter">SPORTS MPS · 주니어골든에이지 <b>대표 이정욱</b></div>', S[0]['body'])
public_sources={
 1:'',2:'',3:'',
 4:link('https://www.kci.go.kr/kciportal/landing/article.kci?arti_id=ART002756163','유상석·서장원(2021), 조기 중도탈락 연구')+' · 이탈 경로 개념도 · 43%+ 원통계 확인 필요',
 5:link(MCST,'문체부 2024년 기준 스포츠산업조사')+' · 시설22.323조 + 서비스25.683조 | 시장 추정: 대상 인원 × 연간 지출 · 범위별 시나리오',
 6:link('https://www.kci.go.kr/kciportal/landing/article.kci?arti_id=ART002756163','유상석·서장원(2021), 조기 중도탈락 연구')+' · 학업·경제·진로 등 복합 요인',
 7:link(PL,'Premier League 바이오밴딩 사례')+' · 골연령: 신체 성숙도 지표 · 임상·예측 정확도 검증 예정',
 8:'가상 선수·예시 데이터 · 효과·정확도 검증 예정',
 9:'의료 진료는 제휴 의료기관 제공',
 10:'측정·평가 건수 · 팀 접점 · 부모325명 설문 기준',
 11:'',
 12:'운영 가정: 본사 측정·개발 지원 · 본사 공용원가 별도 관리',
 13:'요금·거점 수·가동률은 계획 가정 · 공동광고 별도 정산 · 초기 가맹비 및 기관 자체 진료 매출 제외',
 14:'계획 가정: 센터별 회원120명·월40만 원·별도 측정40명 | 운영 잉여: 본사 공용비·감가·세금 전',
 15:link(PLCO,'PLCO')+' · '+link(PLGYM,'플코짐')+' · '+link(AR,'ARROWZ LAB')+' · 공개 서비스 기준',
 16:link(PLCO,'PLCO 팀 멤버십')+' · '+link(PLGYM,'플코짐')+' · 공개 서비스 기준',
 17:link(PL,'Premier League')+' · '+link(AR,'ARROWZ LAB')+' · '+link(ARG,'ARROWZ GYM')+' · 해외 교류·제휴·진출 (예정)',
 18:link(ARG,'ARROWZ: 연간 측정·월간 테스트·주간 훈련·앱')+' · MPS 운영 적용 (예정)',
 19:'',
 20:'20억 원 · 18개월 예산 계획안 · 라운드 금액·조건 협의 예정',
 21:'',22:'',23:'현장 접점·협력 네트워크',24:'',
}
for r in S:r['source']=public_sources[r['no']]
REFERENCE_CSS+='''
.cover-tags{margin-top:24px}
.cover-tags span{font-size:19px;padding:12px 20px}
.cover-tags b{font-weight:800}
.cover-presenter{margin-top:28px;font-size:29px;line-height:1.4;color:var(--ink)}
.cover-presenter b{font-weight:800;margin-left:10px}
.cover footer .brand{visibility:hidden}
'''
