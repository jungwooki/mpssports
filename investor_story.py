# -*- coding: utf-8 -*-
# Explain the customer, the report and the revenue model to a non-specialist investor.
BASE_STORY=S[:]
def rewrite(i,title,sub,body=None):
 r=BASE_STORY[i-1]
 r['title']=title;r['sub']=sub
 if body is not None:r['body']=body
 return r
rewrite(3,'아이의 성장을 돕는 일이, <em>어떻게 사업이 될까요?</em>','부모가 이해할 리포트에서 시작해, 상담과 운동 관리로 이어집니다.')
rewrite(4,'축구를 좋아하던 아이가, <em>왜 그만두게 될까요?</em>','중학교 진입기에는 몸의 성장 차이, 통증, 비교의 부담이 함께 커질 수 있습니다.')
rewrite(5,'축구에서 시작해, <em>성장기 선수의 관리 시장으로</em>','선수 수와 1년 관리비로 계산했습니다. 활동 아동까지 확장하면 1.2조 원 시나리오입니다.')
rewrite(6,'부모도 지도자도, <em>판단할 근거가 필요합니다</em>','고객이 비용을 낼 이유는, 아이에게 지금 필요한 도움을 구체적으로 알기 위해서입니다.',
 '<div class="investor-anxiety">'+table(['무슨 고민이 있나요?','부모의 질문','지도자의 질문'],[['성장','왜 우리 아이만 작을까요?','더 기다려도 될까요?'],['몸 상태','아픈데 계속 뛰어도 될까요?','훈련을 늘릴까요, 줄일까요?'],['마음','실수하면 왜 위축될까요?','어떻게 격려해야 할까요?']])+band('MPS가 연결합니다 <b>측정 → 이해할 수 있는 리포트 → 전문가의 지원</b>')+'</div>')
rewrite(7,'바이오밴딩, <em>비슷한 성장단계끼리 함께 봅니다</em>','생년월일로 묶던 선수를 신체의 성숙도로도 묶어보는 접근입니다. MPS는 이 관점을 리포트에 적용합니다.')
BASE_STORY[3]['body']=BASE_STORY[3]['body'].replace('초기 장표 인용','중학교 전후 이탈').replace('중학교 전후 탈락률로 제시','탈락률 참고 수치')
BASE_STORY[6]['body']=BASE_STORY[6]['body'].replace('현재 체격에 가려진 <b>성장의 맥락</b>을 함께 봅니다.','MPS의 차별점 <b>같은 나이 + 성장단계 + 지난 기록</b>을 함께 읽습니다.')
rewrite(10,'현장에서는 이미 만나고 있습니다. <em>이제 유료 고객으로</em>','쌓아온 접점과 검사 의향을 바탕으로, 실제 구매와 재구매를 검증하겠습니다.')
rewrite(11,'리포트 다음의 도움, <em>실행할 사람들이 있습니다</em>','의료, 스포츠, 심리, 기술 인력이 측정 결과를 실제 서비스로 연결합니다.')
rewrite(12,'먼저 서울 한 곳에서, <em>계속 찾는 이유를 만들겠습니다</em>','부모가 월 관리비를 내고, 선수가 정기적으로 도움받는 운영 모델을 검증합니다.')
BASE_STORY[11]['body']=BASE_STORY[11]['body'].replace('월40만 원 환산','월 관리비40만 원 가정').replace('측정 → 관리 → 멤버십','부모가 결제 → 스튜디오에서 관리 → 변화를 보고 재방문')
rewrite(13,'센터가 늘어날 때, <em>본사에도 반복 매출이 생깁니다</em>','제휴기관이 리포트 소프트웨어와 운영 지원을 월 구독합니다. SaaS는 이 소프트웨어 구독료입니다.')
BASE_STORY[12]['body']=BASE_STORY[12]['body'].replace('SaaS50 + 인증 운영30','소프트웨어50 + 인증 운영30').replace('SaaS30 + 운영지원20','소프트웨어30 + 운영지원20')
rewrite(14,'한 번의 검사에서, <em>꾸준한 관리 매출로</em>','부모의 관리비, 팀 계약, 제휴기관 구독료를 더한 2027–2031 매출 시나리오입니다.')
rewrite(15,'잘 뛰는지만 볼까요? <em>어떻게 자라는지도 봅니다</em>','성장단계를 해석하고, 몸과 마음의 지원까지 연결하는 것이 MPS의 집중 영역입니다.')
rewrite(16,'고객이 MPS를 고를 이유, <em>성장기를 함께 본다는 것</em>','피지컬 측정에 성장단계와 멘탈 해석을 더하고, 필요한 전문가에게 연결합니다.')
rewrite(17,'해외에서는 이미, <em>측정과 훈련을 연결하고 있습니다</em>','영국의 바이오밴딩과 일본의 측정 서비스에서 배우고, 국내 성장기 선수에게 맞춥니다.')
rewrite(18,'측정이 다음 훈련으로 이어지면, <em>다시 만날 이유가 생깁니다</em>','일본 ARROWZ는 측정, 훈련, 기록을 연결합니다. MPS는 여기에 성장단계 기반 통합 지원을 설계합니다.')
rewrite(19,'지도자는 축구에 집중하고, <em>MPS는 성장을 돕습니다</em>','선수 곁에서 몸과 마음의 변화를 살피고, 필요한 도움을 연결하겠습니다.')
rewrite(20,'투자를 받으면, <em>이 세 가지를 제대로 만들겠습니다</em>','전문인력, 제품, 서울 센터를 갖춰 반복 가능한 운영 모델을 증명하겠습니다.')
rewrite(21,'사람을 모으고 현장을 움직여온 <em>팀입니다</em>','대표의 임상 경험과 현장 네트워크에, 스포츠와 심리, 개발 역량을 더했습니다.')
rewrite(22,'선수마다 다른 성장의 시간, <em>사업의 기회도 여기에 있습니다</em>','서울에서 운영을 증명하고, 전국의 부모와 팀이 이용하는 성장관리 플랫폼으로 나아갑니다.')
rewrite(23,'첫 고객은 어디서 만날까요? <em>축구 현장에 있습니다</em>','쌓아온 팀 네트워크를 측정 행사, 리포트 상담, 관리 프로그램의 접점으로 연결하겠습니다.')
rewrite(24,'아이와 부모가 있는 곳에서, <em>MPS는 시작했습니다</em>','측정하고, 설명하고, 다음 도움을 연결해 온 현장입니다.')

def service(cat,title,sub,page_name,focus_name,focus_caption,insight,details,route,payer,notes):
 body='<div class="report-story"><figure class="report-whole"><button class="zoom">'+pic(A/page_name,'가상 선수 리포트 전체 보기')+'</button><figcaption>제작 중인 리포트 샘플</figcaption></figure><div class="report-explain"><div class="report-top"><figure class="report-detail"><button class="zoom">'+pic(A/focus_name,focus_caption)+'</button><figcaption>'+focus_caption+'</figcaption></figure><div class="report-reading"><small>이 리포트에서 읽는 것</small><h2>'+insight+'</h2>'+''.join('<div><b>'+str(i+1).zfill(2)+'</b><span>'+x+'</span></div>' for i,x in enumerate(details))+'</div></div><div class="report-service"><small>서비스는 이렇게 이어집니다</small><div>'+''.join('<span>'+x+'</span>'+('<i>→</i>' if i<len(route)-1 else '') for i,x in enumerate(route))+'</div></div><div class="report-payment"><span>매출 연결</span><strong>'+payer+'</strong><small>사업 모델 계획</small></div></div></div>'
 return dict(no=0,cat=cat,title=title,sub=sub,body=body,source='가상 선수의 예시 데이터 | 리포트와 프로그램 고도화 중 | 서비스 효과 검증 예정',cls='report-investor',notes=notes)
reports=[
 service('해결 방법 / M 멘탈 1','실수 한 번에 위축되는 아이, <em>무엇을 도와줄까요?</em>',
 '멘탈 리포트는 경기 중 마음의 강점과 연습할 부분을 정리해, 상담의 출발점을 만듭니다.',
 'mental-2.png','mental-focus.png','준비 능력과 실수 후 회복을 나란히 봅니다',
 '잘하는 것과<br><em>도울 것을 구체적으로.</em>',
 ['경기 준비, 긴장, 회복을 확인','같은 성장단계와 또래로 비교','부모와 코치의 대화를 돕는 자료'],
 ['멘탈 측정','리포트 설명','상담 계획'],
 '부모의 평가 비용 → 본사 상담 프로그램',
 '투자자 설명: 축구 기술은 좋아도 평가나 실수 앞에서 위축될 수 있다. 멘탈 리포트는 막연한 걱정을 구체적인 상담 주제로 바꾸는 제품이다. 예시에서는 준비 능력과 실수 후 회복이 다르게 나타난다. 성장단계와 멘탈의 연결은 제품 설계 관점이며, 뼈나이로 심리 발달을 판정하지 않는다. 비교 기준과 프로그램 효과는 별도 검증 대상이다. 첨부 멘탈 리포트 2쪽 상세, 3쪽에 또래 비교. 부모 결제 및 본사 상담 수익은 사업 모델 계획.'),
 service('해결 방법 / M 멘탈 2','상담에서 정한 연습을, <em>다음 리포트로 확인합니다</em>',
 '한 번의 설명 뒤에도 전문가의 멘토링과 작은 행동 기록으로 관리를 이어갑니다.',
 'mental-4.png','mental-followup.png','전문가 상담과 생활 속 연습을 연결하는 화면',
 '다음에 해볼 행동을<br><em>함께 정합니다.</em>',
 ['본사 심리상담과 멘토링 연결','부모와 지도자가 지원 방향 공유','다시 측정해 변화와 다음 과제 확인'],
 ['본사 상담','작은 행동 연습','재측정과 리뷰'],
 '부모의 멘토링 이용료 → 재상담과 정기 평가',
 '투자자 설명: 리포트는 상담을 시작할 공통 자료이며, 전문가 지원과 반복 리뷰가 다음 구매 이유를 만든다는 가설이다. 출시 예정 모바일 다이어리는 일상 기록 접점이다. 재구매율이 입증되었다고 주장하지 않는다. 상담 전환율, 프로그램 완료율, 재구매율을 운영 검증 지표로 삼는다. 원본은 멘탈 리포트 4쪽.'),
 service('해결 방법 / P 피지컬 1','더 뛰게 할지 쉬게 할지, <em>몸의 기록부터 봅니다</em>',
 '부모와 지도자가 따로 보던 몸 상태를 한 리포트에 모아, 전문가와 살펴볼 지점을 정리합니다.',
 'physical-2.png','physical-body.png','좌우 차이와 초음파 기록을 함께 확인합니다',
 '어디를 살펴볼지<br><em>대화가 구체적으로.</em>',
 ['체격과 체수분 등 측정값 정리','좌우 기록과 이전 기록 비교','불편감은 의료기관의 상담으로'],
 ['몸 상태 측정','전문가 설명','진료 또는 운동 관리'],
 '평가 서비스 → 스튜디오 관리와 제휴기관 구독',
 '투자자 설명: 서비스는 흩어진 신체 기록을 설명 가능한 리포트로 연결한다. 신체검사와 초음파 판독은 해당 전문인력과 의료기관의 역할이다. 리포트의 샘플 지수와 색상은 임상 확진이나 부상 확률을 뜻하지 않는다. 해당 의료기관의 진료비는 의료기관 매출이며 MPS는 평가, 스튜디오 관리 및 기관 대상 소프트웨어 구독 모델을 설계한다. 첨부 피지컬 리포트 2쪽.'),
 service('해결 방법 / P 피지컬 2','무엇을 강화할지 보이면, <em>스튜디오에서 돕습니다</em>',
 '점프와 근력, 균형을 측정하고 운동 계획을 세웁니다. 다음 측정에서는 지난 자신과 비교합니다.',
 'physical-3.png','physical-action.png','수행 능력을 측정하고 강화할 영역을 정합니다',
 '측정 다음에<br><em>운동 계획이 생깁니다.</em>',
 ['성장단계와 좌우 차이 함께 해석','코치가 개별 컨디셔닝 계획 수립','회차별 관리와 재측정으로 리뷰'],
 ['수행 능력 측정','개별 컨디셔닝','재측정과 계획 조정'],
 '부모의 월 관리비40만 원 × 활성회원120명',
 '투자자 설명: 컨디셔닝은 몸의 기능과 운동 수행을 관리하는 프로그램이다. 훈련 이후 관리와 리뷰를 운영해 월 관리비 또는 회차권 형태의 반복 매출을 검증한다. 월40만 원은 120명 활성회원의 월평균 환산 가정이다. 재활 회차권 등의 이용 편차를 포함할 수 있으나 의료행위는 해당 기관 역할로 구분한다. 리포트 3쪽의 수행검사 수치와 비교 평균은 모두 가상 예시이며 실제 서비스 효과를 입증하지 않는다.'),
 service('해결 방법 / S 성장단계','같은 13세여도, <em>몸이 자라는 시간은 다릅니다</em>',
 '나이, 뼈의 성숙도, 성장단계를 함께 보여줍니다. 지금의 체격을 이해하는 기준부터 바꿉니다.',
 'physical-1.png','growth-stage.png','실제 나이와 뼈나이, 성장단계를 함께 보여줍니다',
 '성장단계가<br><em>관리의 기준이 됩니다.</em>',
 ['어느 성장 시기인지 함께 확인','멘탈과 피지컬 해석의 공통 맥락','의료기관 상담과 다음 측정 연결'],
 ['성장 측정','의료기관 상담','성장 추적'],
 'MPS의 평가 및 기관 구독 / 진료비는 의료기관',
 '투자자 설명: 바이오밴딩은 생물학적 성숙도를 반영해 집단을 구성하는 접근이며 MPS는 이를 종합성장관리의 해석 기준으로 확장하려 한다. 골연령만으로 성장단계를 확정하거나 최종 신장 및 심리 발달을 예측한다고 주장하지 않는다. 성장단계 증거 화면은 제공된 피지컬 리포트 첫 페이지를 사용했다. 독립 성장 리포트 완제품으로 오인하지 않도록 제목과 캡션을 구성했다. 멘탈/피지컬 원본의 단계 번호 체계가 달라 이 장표에서는 단계 명칭 위주로 설명한다. 기관 자체 진료 매출은 MPS 재무 모델에서 제외한다.'),
]
S=BASE_STORY[:7]+reports+BASE_STORY[9:]
for i,r in enumerate(S,1):r['no']=i
assert len(S)==27
# Keep the reference chapter order and update printed page ranges.
toc=[('목차','01'),('요약','02'),('시장 현황 및 문제','03–06'),('해결 방법 / 리포트와 서비스','07–11'),('성과 (요약 및 상세)','12–13'),('확장 전략','14–15'),('향후 매출 목표','16'),('경쟁사 분석','17–20'),('미션 / 투자금 사용계획','21–22'),('팀원 소개','23'),('마무리','24'),('Appendix','25–26')]
S[1]['body']='<div class="reference-toc">'+''.join(f'<div><span>{i+1}. {a}</span><i></i><b>{n}</b></div>' for i,(a,n) in enumerate(toc))+'</div>'
S[2]['body']=S[2]['body'].replace('>WHO<','>대상<').replace('투자 → 실행 기반','투자가 만드는 실행 기반')
S[14]['body']=S[14]['body'].replace('현재 운영 센터 서울 R&D 센터 구축 예정','현재 운영 센터 / 서울 R&D 센터 구축 예정')
# Make the revenue collection route explicit in the network slide.
S[15]['body']=S[15]['body'].replace('SaaS50 + 인증 운영30','소프트웨어50 + 인증 운영30').replace('SaaS30 + 운영지원20','소프트웨어30 + 운영지원20')
S[16]['notes']+='\n투자자 설명: 부모는 평가와 관리 프로그램을, 팀은 계약 서비스를, 제휴기관은 소프트웨어와 운영 지원을 구매하는 구조다. 수치가 상승하는 이유는 단가 인상만이 아니라 직영센터, 기관 구독, 독립 평가와 멘탈 구매자가 함께 늘어나는 계획 때문이다. 240억원은 이 조건들이 충족될 때의 시나리오다.'
S[19]['notes']+='\n투자자 설명: 해외 사례는 문제 해결 방식과 운영 구조의 선행 참고다. 국내 수요나 MPS 제휴 실적의 증거로 전환하지 않는다.'
S[22]['body']=S[22]['body'].replace('R&D·전문인력','R&D와 전문인력').replace('R&D 전문인력','R&D와 전문인력')
S[24]['body']=S[24]['body'].replace('부모에게는 근거를.<br>지도자에게는 지원을.<br>선수에게는 성장의 시간을.','부모가 이해하고,<br>전문가가 돕고,<br>선수가 다시 찾는 서비스.')
# Keep the established title, source and punctuation rules.
for r in S:
 assert '<br' not in r['title']
 for k in ('title','sub','cat','body','source'):
  parts=re.split(r'(<[^>]*>)',r[k])
  for i in range(0,len(parts),2):parts[i]=re.sub(r'\s*[·ㆍ]\s*',' ',parts[i])
  r[k]=''.join(parts)
REFERENCE_CSS+='''
.report-investor .content{top:237px;bottom:116px}
.report-story{display:grid;grid-template-columns:342px 1fr;gap:32px;height:535px}
.report-whole{margin:0;background:#f5f5f7;border:1px solid #e6e6eb;border-radius:18px;padding:14px;display:flex;flex-direction:column;align-items:center}
.report-whole .zoom{height:467px;width:100%;background:transparent;padding:0;border:0;box-shadow:none}
.report-whole img{height:100%;width:100%;object-fit:contain}
.report-whole figcaption{font-size:16px;margin-top:12px;color:#73737c}
.report-explain{display:flex;flex-direction:column;gap:18px;min-width:0}
.report-top{display:grid;grid-template-columns:1.25fr 1fr;gap:24px;min-height:313px;align-items:start}
.report-detail{margin:0;border:1px solid #e1e1e7;border-radius:16px;overflow:hidden;background:#f8f8fa;padding:14px}
.report-detail .zoom{width:100%;height:254px;border:0;padding:0;background:transparent;box-shadow:none}
.report-detail img{width:100%;height:100%;object-fit:contain}
.report-detail figcaption{font-size:17px;text-align:center;line-height:1.4;margin-top:10px;color:#62626c}
.report-reading{padding:5px 0}
.report-reading>small{font-size:16px;color:#73737c}
.report-reading h2{font-size:31px;line-height:1.42;margin:15px 0 20px;letter-spacing:-.6px}
.report-reading>div{display:flex;gap:12px;margin-top:13px;align-items:baseline;font-size:20px;line-height:1.55;word-break:keep-all}
.report-reading>div>b{font-size:13px;color:#8874b8}
.report-service{background:#f5f5f8;border-radius:16px;padding:14px 22px}
.report-service>small{font-size:15px;color:#73737c}
.report-service>div{display:flex;align-items:center;justify-content:space-between;gap:14px;margin-top:14px}
.report-service span{font-size:24px;font-weight:700;white-space:nowrap}
.report-service i{font-style:normal;color:#fc582b;font-size:26px}
.report-payment{margin-top:auto;border-top:1px solid #ddddE4;padding:19px 0 7px;display:flex;align-items:center;gap:15px}
.report-payment>span{font-size:15px;color:#fc582b;white-space:nowrap}
.report-payment strong{font-size:23px;line-height:1.35;word-break:keep-all}
.report-payment>small{font-size:13px;color:#777782;margin-left:auto;white-space:nowrap}
.investor-anxiety .band{font-size:24px;margin-top:26px}
.investor-anxiety .band b{display:block;margin-top:8px}
.center-reference .band{font-size:23px;line-height:1.5}
.network-reference .card p{font-size:18px}
'''
# Founder-defined differentiation: specify the assessment basis of each service.
S[2]['sub']='멘탈은 바이오밴딩 + 인지검사, 피지컬은 바이오밴딩 + 기능평가를 기반으로 관리합니다.'
S[2]['body']=S[2]['body'].replace('<strong>멘탈</strong><span>본사 상담</span>','<strong>멘탈</strong><span>본사 상담</span><small class="domain-basis">바이오밴딩 + 인지검사</small>').replace('<strong>피지컬</strong><span>스튜디오</span>','<strong>피지컬</strong><span>스튜디오</span><small class="domain-basis">바이오밴딩 + 기능평가</small>').replace('<strong>성장 측정</strong><span>의료기관</span>','<strong>성장 측정</strong><span>의료기관</span><small class="domain-basis">성장단계 해석</small>')
S[6]['body']=re.sub(r'<div class="band">.*?</div>$','<div class="assessment-bases"><div><small>M 멘탈</small><strong>바이오밴딩 + 인지검사</strong></div><div><small>P 피지컬</small><strong>바이오밴딩 + 기능평가</strong></div></div>',S[6]['body'])
S[7]['title']='멘탈은 <em>바이오밴딩 + 인지검사 기반입니다</em>'
S[7]['sub']='실수 한 번에 위축되는 아이에게 무엇을 도울까요? 성장단계와 인지검사를 함께 살핍니다.'
S[7]['body']=S[7]['body'].replace('잘하는 것과<br><em>도울 것을 구체적으로.</em>','성장단계에<br><em>인지검사를 더합니다.</em>').replace('경기 준비, 긴장, 회복을 확인','인지검사를 기반으로 멘탈 해석').replace('멘탈 측정</span>','인지검사</span>')
S[8]['sub']='바이오밴딩 + 인지검사 기반의 멘탈 해석을 본사 상담과 멘토링, 다음 리포트로 연결합니다.'
S[9]['title']='피지컬은 <em>바이오밴딩 + 기능평가 기반입니다</em>'
S[9]['sub']='더 뛰게 할지 쉬게 할지 고민될 때, 성장단계와 몸의 기능을 함께 보고 관리 방향을 정합니다.'
S[9]['body']=S[9]['body'].replace('어디를 살펴볼지<br><em>대화가 구체적으로.</em>','성장단계에<br><em>기능평가를 더합니다.</em>').replace('체격과 체수분 등 측정값 정리','기능평가와 몸 상태 기록을 연결')
S[10]['sub']='바이오밴딩 + 기능평가를 기반으로 점프와 근력, 균형을 해석하고 개별 운동 계획을 세웁니다.'
S[10]['body']=S[10]['body'].replace('수행 능력 측정</span>','기능평가</span>')
S[17]['sub']='멘탈은 바이오밴딩 + 인지검사, 피지컬은 바이오밴딩 + 기능평가로 읽고 전문가의 지원을 연결합니다.'
S[18]['title']='MPS의 차별점, <em>성장단계에 검사와 평가를 더합니다</em>'
S[18]['sub']='멘탈과 피지컬을 각각 다른 검사 기반으로 해석하고, 상담과 컨디셔닝으로 연결합니다.'
S[18]['body']=table(['구분','PLCO / 공개 서비스','MPS / 집중 영역'],[
 ['대상','유소년 및 엘리트 팀','10–15세 성장기 선수'],
 ['피지컬','피지컬 측정, 리포트, 훈련','바이오밴딩 + 기능평가 기반'],
 ['멘탈','공개 서비스 범위 참고','바이오밴딩 + 인지검사 기반'],
 ['후속 서비스','앱, 웹, 오프라인 짐','의료기관, 본사 상담, 스튜디오'],
])
for i in (2,6,7,8,9,10,17,18):
 S[i]['notes']+='\n대표 지시로 차별화 기반을 명확화: 피지컬은 바이오밴딩 + 기능평가 기반, 멘탈은 바이오밴딩 + 인지검사 기반. 첨부 샘플 화면은 그대로 활용했다. 인지검사 도구명, 문항, 측정 정확도 및 임상 검증 결과는 이번 수정에서 새로 단정하지 않았다.'
REFERENCE_CSS+='''
.summary-domains .domain-basis{grid-column:1/-1;display:block;margin-top:11px;padding-top:9px;border-top:1px solid #dddde4;font-size:15px;color:#676771;white-space:nowrap;letter-spacing:-.3px}
.assessment-bases{display:grid;grid-template-columns:1fr 1fr;gap:22px;margin-top:25px}
.assessment-bases>div{padding:20px 25px;border-radius:16px;background:#f5f5f7;display:flex;align-items:center;gap:24px}
.assessment-bases small{color:var(--purple);font-size:20px;font-weight:700}
.assessment-bases strong{font-size:28px}
'''
# Founder-provided traction: 950 comprehensive growth records accumulated in five months.
S[12]['title']='압도적 <em>데이터 누적속도</em>'
S[12]['sub']='성장종합데이터 950건 / 5개월'
S[12]['body']='<div class="data-traction"><div><article class="data-headline"><small>성장종합데이터</small><strong>950<span>건</span><i>/</i>5<span>개월</span></strong><p>월평균 190건 축적</p></article><div class="data-secondary">'+stat('40여 팀','현장 네트워크','팀과 선수의 접점')+stat('83.1%','부모 검사 의향','325명 설문')+'</div></div>'+fig('추가PPT/image20.jpeg','팀과 선수를 만나 쌓아가는 성장 기록')+'</div>'
S[12]['source']='성장종합데이터 누적 건수 기준 | 월평균190건 = 950건 ÷ 5개월 | 부모325명 검사 의향 설문'
S[12]['notes']+='\n대표 제공 최신 지표: 성장종합데이터950건/5개월. 월평균190건은 단순 산술 평균이다. 고유 선수 수, 유료 고객 수 또는 시계열 가속률로 해석하지 않는다. 압도적이라는 표현은 대표의 핵심 메시지이며 별도의 경쟁사 수집 속도 비교 수치는 제시하지 않는다.'
REFERENCE_CSS+='''
.data-traction{display:grid;grid-template-columns:1fr 660px;gap:42px;align-items:start}
.data-headline{background:#f5f5f7;border-radius:20px;padding:29px 32px}
.data-headline>small{font-size:24px;font-weight:700}
.data-headline>strong{display:block;font-size:90px;line-height:1.3;letter-spacing:-3px;color:var(--orange);margin-top:14px;white-space:nowrap}
.data-headline strong span{font-size:34px;letter-spacing:-1px;margin-left:7px}
.data-headline strong i{font-style:normal;color:#cccbd3;font-size:60px;margin:0 24px}
.data-headline p{font-size:22px;margin-top:13px;color:#676771}
.data-secondary{display:grid;grid-template-columns:1fr 1fr;gap:18px;margin-top:20px}
.data-secondary .stat{padding:20px 25px}
.data-secondary .stat strong{font-size:40px}
.data-secondary .stat h3{font-size:23px}
.data-secondary .stat p{font-size:17px}
.data-traction .warm-photo img{height:410px;object-fit:cover}
'''
# Mental support is diary-based mentoring by a former professional athlete.
mentoring_terms={
 '본사 심리상담과 멘토링 연결':'프로선수 출신 멘토의 멘토링',
 '본사 상담 프로그램':'멘탈 멘토링 프로그램',
 '본사 상담':'멘탈 멘토링',
 '상담 계획':'멘토링 계획',
 '재상담과 정기 평가':'정기 멘토링과 재평가',
 '상담과 컨디셔닝':'멘탈 멘토링과 컨디셔닝',
 '선수 출신 심리상담':'프로선수 출신 멘토',
}
for r in S:
 for key in ('title','sub','body','notes'):
  parts=re.split(r'(<[^>]*>)',r[key])
  for i in range(0,len(parts),2):
   for before,after in mentoring_terms.items():parts[i]=parts[i].replace(before,after)
  r[key]=''.join(parts)
S[7]['sub']='바이오밴딩 + 인지검사로 이해한 강점과 연습할 부분을, 프로선수 출신 멘토의 멘토링으로 연결합니다.'
S[7]['body']=S[7]['body'].replace('부모와 코치의 대화를 돕는 자료','멘토가 지원 방향을 정하는 자료')
S[8]=service('해결 방법 / M 멘탈 2',
 '매일의 기록을 보고, <em>프로선수 출신 멘토가 함께합니다</em>',
 '멘탈강화 모바일앱에 매일 또는 격일로 다이어리를 작성하면, 심리상담사인 멘토가 확인하고 멘토링합니다.',
 'mental-4.png','mental-followup.png','프로선수 출신 멘토와 모바일 다이어리의 연결',
 '선수 경험으로 공감하고<br><em>기록을 보며 멘토링.</em>',
 ['매일 또는 격일로 앱에 기록','프로선수 출신 멘토(심리상담사)가 확인','일상의 기록을 바탕으로 개별 멘토링'],
 ['앱에 기록','멘토 확인','개별 멘토링','변화 리뷰'],
 '부모의 멘탈 멘토링 이용료 → 지속 관리',
 '서비스 목적은 일상 속 멘탈강화 멘토링이다. 프로선수 출신 멘토는 심리상담사이며 선수 경험을 바탕으로 지원한다. 선수는 멘탈강화 모바일앱 다이어리를 매일 또는 격일로 작성하고 멘토가 이를 확인해 멘토링한다. 작성 주기와 멘토의 확인/응답 주기는 구분하며, 응답시간이나 상시대기 등을 새로 약속하지 않는다. 바이오밴딩 + 인지검사는 멘탈 해석의 기반이다. 첨부 멘탈 리포트4쪽의 다이어리는 출시 예정으로 표기되어 있으므로 장표에서도 이를 유지한다. 사업 모델은 프로그램 이용료와 지속 관리다.')
S[8]['no']=9
S[8]['source']='멘탈강화 모바일앱 출시 예정 | 가상 선수 리포트 샘플 | 멘토링 운영 모델 고도화 중'
S[8]['cls']+=' mentoring-model'
S[18]['body']=S[18]['body'].replace('의료기관, 멘탈 멘토링, 스튜디오','의료기관, 프로선수 출신 멘토, 스튜디오')
S[26]['notes']+='\n현장의 리포트 설명에서 멘탈강화 모바일앱 기록과 프로선수 출신 멘토의 멘토링으로 고객 관계를 이어가는 계획이다.'
REFERENCE_CSS+='''
.mentoring-model .report-reading h2{font-size:29px}
.mentoring-model .report-reading>div{font-size:19px}
.mentoring-model .report-service span{font-size:23px}
.mentoring-model .report-service i{font-size:22px}
'''
# Founder-provided expert network caption.
old_caption='전문가 워크숍 기존 사업자료'
assert old_caption in S[13]['body']
S[13]['body']=S[13]['body'].replace(old_caption,'전문가 네트워크, 한의사 봉사대기 70명 이상')
S[13]['notes']+='\n대표 제공 네트워크 현황: 한의사 봉사대기70명 이상. 사진 설명에 반영했으며 실제 봉사 참여 완료 인원과 구분한다.'
# Overseas reference cards with official identity assets and separated roadmap.
S[19]['cls']='overseas-logos'
items=[('ENGLAND / PREMIER LEAGUE','premier-league-logo.svg','Premier League','성장단계로 경기 집단 구성','비슷한 성숙도의 선수들이<br>함께 뛰는 바이오밴딩 사례'),('JAPAN / ARROWZ LAB','arrowz-lab-logo.svg','ARROWZ LAB','측정으로 현재 상태 이해','기초체력을 측정하고 분석해<br>개별 과제를 설명'),('JAPAN / ARROWZ GYM','arrowz-gym-logo.svg','ARROWZ GYM','훈련과 재측정을 연결','측정 결과를 바탕으로 훈련하고<br>기록으로 변화를 확인')]
S[19]['body']='<div class="overseas-cards">'+''.join('<article><small>'+country+'</small><div class="official-logo">'+pic(A/name,label)+'</div><h2>'+title+'</h2><p>'+desc+'</p></article>' for country,name,label,title,desc in items)+'</div><div class="overseas-roadmap"><div class="roadmap-heading"><b>MPS 적용 계획</b><span>교류와 현지화부터 단계적으로 추진 (예정)</span></div>'+flow([('교류','운영과 연구'),('현지화','기준과 언어'),('파일럿','수요와 재현성'),('진출','파트너 계약')])+'</div>'
S[19]['source']=link(PL,'Premier League 바이오밴딩')+' / '+link(AR,'ARROWZ LAB')+' / '+link('https://www.sports-science.co.jp/arrowz-gym/','ARROWZ GYM')+' | 해외 선행 사례'
S[19]['notes']+='\n로고는 각 기관의 공식 웹사이트에서 가져왔다. 해외 선행 사례를 설명하는 용도이며 MPS와의 체결 실적으로 제시하지 않는다.'
# Printed page21: operating network, without a repeated presenter signature.
S[21]['body']=re.sub(r'<div class="mission-sign">.*?</div>','',S[21]['body'])
S[21]['body']=re.sub(r'<p>.*?</p>','<p class="mission-partners">본사 × 의료기관 × 스튜디오 × 멘탈멘토링</p>',S[21]['body'],count=1)
REFERENCE_CSS+='''
.overseas-logos .content{top:244px}
.overseas-cards{display:grid;grid-template-columns:repeat(3,1fr);gap:26px}
.overseas-cards article{height:322px;padding:24px 28px;background:#f6f6f8;border:1px solid #e5e5e9;border-radius:20px}
.overseas-cards article>small{font-size:14px;color:#73737c;letter-spacing:.5px}
.official-logo{height:116px;display:flex;align-items:center;justify-content:center;margin:9px 0 12px;background:white;border-radius:12px}
.official-logo img{width:310px;height:76px;object-fit:contain}
.overseas-cards h2{font-size:28px;line-height:1.3;margin:0 0 13px;letter-spacing:-.5px}
.overseas-cards p{font-size:21px;line-height:1.5;color:#676771}
.overseas-roadmap{margin-top:30px;padding-top:20px;border-top:1px solid #dddde3}
.roadmap-heading{display:flex;gap:22px;align-items:center;margin-bottom:15px}
.roadmap-heading b{font-size:22px}.roadmap-heading span{font-size:17px;color:#73737c}
.overseas-roadmap .flow{gap:26px}
.overseas-roadmap .flow article{padding:14px 20px;background:#f6f6f8}
.overseas-roadmap .flow h3{font-size:25px;margin:6px 0}
.overseas-roadmap .flow p{font-size:18px}
.mission-reference .mission-partners{font-size:25px;white-space:nowrap;letter-spacing:-.4px}
'''

REFERENCE_CSS+='''
.overseas-cards article>small{font-size:15px;font-weight:700;letter-spacing:.3px}
.official-logo img{width:295px;height:73px}
.overseas-cards article:first-child .official-logo img{width:320px}
.overseas-roadmap{margin-top:38px;padding-top:16px}
'''
# Make the domestic comparison discoverable in slide titles and the contents menu.
S[18]['title']='플코(PLCO)와 MPS, <em>성장관리의 초점이 다릅니다</em>'
S[18]['cat']='경쟁사 분석 / 플코 비교'
S[18]['body']=S[18]['body'].replace('PLCO / 공개 서비스','플코(PLCO) / 공개 서비스')

# User-provided image concepts recovered byte-for-byte from earlier source decks.
S[8]['body']=S[8]['body'].replace(pic(A/'mental-followup.png','프로선수 출신 멘토와 모바일 다이어리의 연결'),pic(A/'mental-mentor.jpg','멘탈 멘토와 선수의 상담 이미지'))
S[8]['body']=S[8]['body'].replace('<figcaption>프로선수 출신 멘토와 모바일 다이어리의 연결</figcaption>','<figcaption>선수 경험으로 공감하는 멘탈 멘토링</figcaption>')
S[8]['cls']+=' mentor-photo'
S[14]['body']='<div class="center-concepts">'+''.join('<figure><button class="zoom">'+pic(A/name,title)+'</button><figcaption><b>'+title+'</b><span>상상도 / 구축 예정</span></figcaption></figure>' for name,title in [('measurement-concept.jpg','측정으로 이해하고'),('physical-gym-concept.jpg','맞춤 운동으로 강화합니다')])+'<aside><small>서울 플래그십 월 운영 가정</small><strong>120명</strong><p>활성회원 × 월 40만 원</p><strong>40명</strong><p>월 별도 측정</p><div>직접 인건비 <b>600만 원</b><br>본사 측정팀과 개발 지원</div></aside></div>'+band('측정 → 개별 관리 → 재측정 <b>변화를 확인하며 다시 찾는 스튜디오</b>')
S[14]['source']='시설 상상도 / 서울 센터 구축 예정 | 회원 수와 단가는 운영 가정'
S[21]['body']='<div class="town-concept"><figure><button class="zoom">'+pic(A/'sports-town-concept.png','종합 MPS 스포츠타운 상상도')+'</button><figcaption>종합 MPS 스포츠타운 / 장기 구상 상상도</figcaption></figure><div><small>서울에서 시작해, 장기적으로</small><h2>측정과 강화가<br>한곳에서 이어지는<br><em>MPS 스포츠타운</em></h2><p>본사 × 의료기관 × 스튜디오<br>× 멘탈멘토링</p><div class="town-steps">서울 플래그십 → 제휴 네트워크<br>→ 종합 스포츠타운</div></div></div>'
S[21]['source']='장기 비전 상상도 | 이미지 속 면적과 배치는 구상 예시'
S[21]['notes']+='\n사용자 제공 스포츠타운 상상도를 장기 비전으로 배치했다. 이미지에 포함된 면적과 시설 배치는 확정 계획이 아니다. 이번 투자금 사용계획은 다음 장표의 서울 플래그십과 전문 조직을 기준으로 한다.'
REFERENCE_CSS+='''
.mentor-photo .report-detail img{object-fit:contain;height:254px;width:100%}
.center-concepts{display:grid;grid-template-columns:1fr 1fr .8fr;gap:24px;margin-bottom:25px}
.center-concepts figure,.town-concept figure{margin:0;background:#f6f6f8;border-radius:16px;overflow:hidden}
.center-concepts button,.town-concept button{display:block;border:0;padding:0;background:none;width:100%;cursor:zoom-in}
.center-concepts img{display:block;width:100%;height:318px;object-fit:contain;background:#202126}
.center-concepts figcaption{padding:20px;display:flex;flex-direction:column;gap:9px}
.center-concepts figcaption b{font-size:25px}.center-concepts figcaption span{font-size:16px;color:#67686f}
.center-concepts aside{background:#f6f6f8;border-radius:16px;padding:25px}
.center-concepts aside>small{font-size:17px}.center-concepts strong{display:block;font-size:56px;color:#fc582b;margin-top:17px}
.center-concepts aside p{font-size:23px;margin:5px 0 15px}.center-concepts aside>div{font-size:18px;line-height:1.7;border-top:1px solid #ddd;padding-top:13px}
.town-concept{display:grid;grid-template-columns:690px 1fr;gap:48px;align-items:center;margin-top:-18px}
.town-concept img{display:block;width:100%;height:518px;object-fit:contain;background:#172329}
.town-concept figcaption{padding:14px;text-align:center;font-size:16px;color:#67686f}
.town-concept small{font-size:20px;color:#67686f}.town-concept h2{font-size:43px;line-height:1.45;margin:20px 0}
.town-concept p{font-size:24px;line-height:1.65}.town-steps{font-size:23px;line-height:1.8;margin-top:30px;border-top:2px solid #fc582b;padding-top:20px}
'''
REFERENCE_CSS+='''
.center-concepts .zoom{height:318px}.town-concept .zoom{height:518px}
.center-concepts .zoom img,.town-concept .zoom img{border:0;box-shadow:none}
'''

# 2026-09-23 founder revision: monthly partner charges, in KRW.
for r in model:
 c,p,k=r['clinic_partners'],r['physical_partners'],12*r['partner_ramp']
 r['clinic_saas_krw']=round(c*1000000*k)
 r['clinic_certification_krw']=round(c*1000000*k)
 r['clinic_consumables_agency_krw']=round(c*2000000*k)
 r['physical_saas_krw']=round(p*1000000*k)
 r['physical_support_krw']=round(p*1000000*k)
 r['advertising_agency_krw']=round((c+p)*1000000*k)
 r.pop('advertising_collections_excluded_krw',None)
 revenue_keys=['studio_krw','studio_measurement_krw','clinic_saas_krw','clinic_certification_krw','clinic_consumables_agency_krw','physical_saas_krw','physical_support_krw','advertising_agency_krw','evaluation_krw','mental_krw','team_krw']
 r['total_krw']=sum(r[key] for key in revenue_keys)
last=model[-1];total=last['total_krw']/1e8
for r in S:
 for key in ['title','sub','body','notes','source']:
  r[key]=r[key].replace('239.972',f'{total:.3f}').replace('240억',f'{total:.0f}억')
S[15]['body']='<div class="partner-pricing">'+table(['기관당 월 요금','인증 한의원','피지컬센터'],[['플랫폼 구독','100만 원','100만 원'],['인증운영 / 운영지원','100만 원','100만 원'],['소모품대행','200만 원','—'],['기본 합계','400만 원','200만 원'],['광고대행 (별도)','100만 원','100만 원'],['광고대행 포함','500만 원','300만 원']])+'<aside>'+donut([40.8,20.4,20.4],['한의원 기본 (억)','피지컬 기본 (억)','광고대행 (억)'],'81.6억','연 계약매출 가정')+'<p>한의원 100곳 + 피지컬센터 100곳<br>연평균 가동 85% 시나리오</p></aside></div>'
S[15]['sub']='한의원 월 400만 원, 피지컬센터 월 200만 원에 기관당 광고대행 월 100만 원을 더합니다.'
S[15]['source']='월 요금 계획 | 2031 각 100곳, 가동 85%, 전 기관 광고대행 이용 가정'
S[15]['notes']='대표 지시 단가(만원/월): 인증 한의원 플랫폼100 + 인증운영100 + 소모품대행200 =400. 피지컬센터 플랫폼100 + 운영지원100 =200. 광고대행은 양 기관에 각각 월100의 별도 서비스 요금으로 가정. 광고대행 포함 한의원500, 피지컬300. 2031 각100기관×12개월×85% 기준 한의원 기본40.8억, 피지컬 기본20.4억, 광고대행20.4억, 합계81.6억. 기존 공동광고 분담금 모델을 광고대행 서비스 요금 모델로 교체했다. 소모품대행200 및 광고대행100은 회사 청구 매출 가정이며 비용과 이익을 의미하지 않는다. 매체 광고비나 소모품 매입비가 포함된 총취급액인지에 따라 추후 정산 구조를 확정한다. 초기 가맹비와 기관 자체 진료 및 훈련 매출은 제외.'
S[16]['body']=re.sub(r'<svg.*?</svg>',linechart([str(r['year']) for r in model],[r['total_krw']/1e8 for r in model],'회사 매출 계획 / 억 원'),S[16]['body'],count=1,flags=re.S)
S[16]['sub']=f'부모의 관리비, 팀 계약, 제휴기관 서비스 매출을 더한 2031년 {total:.3f}억 원 시나리오입니다.'
S[16]['source']='기관당 광고대행 월 100만 원 포함 | 요금, 기관 수, 고객 수와 가동률은 계획 가정'
S[16]['notes']+='\n제휴기관 월 요금 갱신: 한의원400만, 피지컬200만, 광고대행 각100만. 2031 제휴기관81.6억을 포함한 전체 매출308.312억. 소모품 및 광고대행 청구액 기준 가정이며 관련 비용을 차감한 이익과 구분한다. 서울 센터 손익 가정은 유지.'
REFERENCE_CSS+='''
.partner-pricing{display:grid;grid-template-columns:1.2fr 1fr;gap:40px;align-items:center}
.partner-pricing table{font-size:23px}.partner-pricing td{padding:16px 20px}.partner-pricing th{font-size:21px;padding:18px 20px}
.partner-pricing tr:last-child td{font-weight:800;background:#fff0e6;color:#202126}
.partner-pricing .donut-layout{grid-template-columns:1fr;justify-items:center;gap:10px}
.partner-pricing svg{height:275px}.partner-pricing .chart-legend{width:390px;font-size:19px}
.partner-pricing aside>p{font-size:19px;line-height:1.6;text-align:center;margin-top:18px;color:#67686f}
'''

# Audit fixes: summary text split by markup, removed cover copy, stale speaker notes.
S[2]['body']=re.sub(r'(<div class="summary-outcome">.*?<small>5년차 매출 시나리오</small><strong>)\d+(<span>억 원</span>)',lambda m:m[1]+f'{total:.0f}'+m[2],S[2]['body'],flags=re.S)
S[0]['body']=re.sub(r'<div class="cover-tags">.*?</div>','',S[0]['body'],flags=re.S)
S[8]['body']=S[8]['body'].replace('이 리포트에서 읽는 것','멘토링은 이렇게 진행합니다')
S[16]['notes']='연도별 회사 매출 시나리오(억원): '+', '.join(f"{r['year']}년 {r['total_krw']/1e8:.3f}" for r in model)+'.\n'
S[16]['notes']+='2031년 구성: 직영 회원97.920억 + 직영 별도 측정9.792억 + 한의원 기본40.800억 + 피지컬센터 기본20.400억 + 광고대행20.400억 + 독립평가72.000억 + 멘탈32.000억 + 팀계약15.000억 =308.312억.\n'
S[16]['notes']+='파트너 월 요금: 한의원 플랫폼100만+인증운영100만+소모품대행200만=400만원. 피지컬센터 플랫폼100만+운영지원100만=200만원. 각 기관 광고대행 월100만원 별도. 각100기관, 연평균 가동85%, 전 기관 광고대행 이용 가정. 소모품대행 및 광고대행은 회사 청구 매출로 가정하며 이익을 의미하지 않는다. 매입비 및 매체비 포함 여부는 계약에서 확정한다. 기관 자체 매출과 초기 가맹비는 제외.\n'
S[16]['notes']+='서울 1개 센터 월 매출: 활성회원120명×40만원=4800만원, 별도 측정40명×12만원=480만원, 팀5곳×연300만원÷12=125만원, 합계5405만원. 인건비600만원+임차600만원+기타500만원+변동비540.5만원=2240.5만원. 운영 잉여3164.5만원은 본사배부, 감가상각, 세금 전. 센터 측정 고객과 독립평가 고객은 별도 고객으로 가정하며 팀 계약은 전체 팀계약 매출에 한 번만 포함. 직영20곳 확대는 추가 조달 및 공급능력 검증을 전제한다.'

# Printed page 17: named adjacent services and a concrete national expansion model.
comparison_sources=[
 ('함소아','https://hamsoa.net/'),
 ('하이키','https://highki.com/kor/clinic/clinic02.php'),
 ('하늘병원','https://www.smcsky.com/content/clinic_08'),
 ('세종스포츠정형외과','https://www.sjsclinic.com/'),
 ('플코','https://plco.pro/gym'),
 ('솔리드 기업 공고','https://spobiz.kspo.or.kr/job/front/job/search/recruit/view.do?recruitSeq=14928'),
 ('마인드카페','https://center.mindcafe.co.kr/')]
S[17]['title']='분야별 전문 서비스를, <em>선수의 성장 여정으로 연결합니다</em>'
S[17]['sub']='10–15세 선수에 집중하는 MPS: 바이오밴딩 기반 리포트와 지역 제휴 운영을 함께 확장합니다.'
S[17]['cat']='경쟁사 분석 / 분야별 비교와 전국 확장'
S[17]['cls']='sector-comparison'
rows=[
 ['성장클리닉','함소아 / 하이키','성장 검사와 진료<br>소아 건강 및 생활 관리','성장단계를 공통 기준으로<br>피지컬과 멘탈 관리까지 연결'],
 ['스포츠 재활','하늘병원<br>세종스포츠정형외과','스포츠 손상 진료<br>재활과 운동 복귀 지원','의료기관의 진료와 연계해<br>일상 컨디셔닝과 성장 추적'],
 ['피지컬센터','플코 / 솔리드','플코: 측정과 훈련, 앱 관리<br>솔리드: 선수 훈련과 재활 트레이닝','바이오밴딩 + 기능평가<br>성장단계별 강화와 재측정'],
 ['멘탈센터','마인드카페','심리검사와 상담<br>지역 센터와 비대면 상담','바이오밴딩 + 인지검사<br>선수 출신 멘토와 일상 기록']]
S[17]['body']='<div class="sector-table">'+table(['분야','비교 기관','공개 서비스의 중심','MPS가 연결할 관리 (계획)'],rows)+'</div><div class="national-heading"><b>전국으로 확장하는 방법</b><span>서울에서 운영 검증 → 지역 제휴기관에 적용 (예정)</span></div><div class="national-route"><article><small>01 / 본사</small><h3>공통 리포트와 교육</h3><p>측정 기준, 해석, 품질관리</p></article><i>→</i><article><small>02 / 지역</small><h3>기존 전문인력과 시설</h3><p>의료기관 × 스튜디오 × 멘토</p></article><i>→</i><article><small>03 / 반복 매출</small><h3>기관 월 계약과 재측정</h3><p>구독과 운영지원, 누적 기록</p></article></div>'
S[17]['source']='2026.09.23 공개 자료 | '+' / '.join(link(url,name) for name,url in comparison_sources)+'<br>서비스 중심 비교 / MPS는 개발 및 운영 고도화 단계 / 전국 제휴 확장 예정'
S[17]['notes']='비교 범위는 공개 서비스의 중심이며 경쟁사의 기능 부재나 MPS의 검증된 임상 우위를 뜻하지 않는다. 함소아는 소아 건강과 성장 진료 및 다지점 운영, 하이키는 성장종합검사와 성장 및 사춘기 관리를 공개한다. 하늘병원과 세종스포츠정형외과는 스포츠 손상 진료 및 재활과 운동 복귀 서비스를 제공한다. 사용자 지칭 세종스포츠클리닉은 공식 의료기관명 세종스포츠정형외과의원으로 표기했다. 플코는 측정, 훈련, 앱 및 팀 관리 서비스를 제공한다. 솔리드는 기업이 직접 게시한 국민체육진흥공단 채용공고에서 엘리트 선수 트레이닝, 스포츠 재활 트레이닝, 축구팀 트레이닝을 확인했다. 마인드카페는 심리검사와 상담, 지역 센터와 비대면 상담을 제공한다. 각 비교 기관은 MPS와 협약한 기관 목록이 아니다. 함소아와 마인드카페 등도 지역 확장 모델을 보유하므로 전국 확장 가능성을 MPS만의 독점적 특성으로 주장하지 않는다.\\nMPS의 전략적 차별화는 10–15세 선수에 집중하고 바이오밴딩을 공통 해석 맥락으로 사용하며 기능평가 및 인지검사 기반 리포트를 지역 전문가의 관리로 연결하려는 운영 설계다. 본사는 서울 플래그십에서 측정 절차, 리포트, 교육과 품질관리 기준을 검증한 뒤 지역의 기존 의료기관과 스튜디오에 적용할 계획이다. 전국 확장 시 모든 시설을 본사가 직접 구축할 필요를 줄이고 기관 구독과 운영지원의 반복 계약을 설계한다. 실제 확장 가능성은 제휴 전환율, 기관별 활성 선수 수, 재측정률, 계약 유지율과 품질관리 비용으로 검증해야 한다. 초기 네트워크 접점과 봉사대기 인원은 유료 제휴계약 실적과 구분한다.\\n확인 출처:\\n'+'\\n'.join(name+': '+url for name,url in comparison_sources)
REFERENCE_CSS+='''
.sector-comparison .content{top:235px;bottom:110px}
.sector-table table{table-layout:fixed;font-size:21px}
.sector-table th{padding:14px 18px;font-size:18px}
.sector-table td{padding:13px 18px;line-height:1.45;vertical-align:middle}
.sector-table th:nth-child(1){width:13%}.sector-table th:nth-child(2){width:23%}.sector-table th:nth-child(3){width:31%}.sector-table th:nth-child(4){width:33%;background:#8874b8}
.sector-table td:last-child{background:#f0edf7;font-weight:700}
.sector-table td:nth-child(2){font-weight:700}
.national-heading{display:flex;align-items:center;gap:25px;margin:20px 0 12px}
.national-heading b{font-size:24px}.national-heading span{font-size:17px;color:#67686f}
.national-route{display:grid;grid-template-columns:1fr 28px 1fr 28px 1fr;gap:13px;align-items:center}
.national-route article{background:#f6f6f8;border-radius:14px;padding:15px 20px}
.national-route small{font-size:14px;color:#8874b8}.national-route h3{font-size:24px;margin:7px 0 3px}
.national-route p{font-size:18px;color:#67686f}.national-route>i{font-style:normal;font-size:28px;color:#fc582b;text-align:center}
.sector-comparison footer .source{font-size:10.5px}
'''
(DOC/'경쟁서비스_비교근거_20260923.md').write_text('# 17페이지 비교 근거\n\n공개 자료 확인: 2026-09-23\n\n'+'\n'.join('- ['+name+']('+url+')' for name,url in comparison_sources)+'\n\n'+S[17]['notes'].replace('\\n','\n'))
S[17]['notes']=S[17]['notes'].replace('\\n','\n')
REFERENCE_CSS+='''
.national-heading{margin-top:16px}
.national-route article{padding:10px 20px}
.national-route h3{margin-top:5px}
'''

# Graphic alternative: qualitative positioning, with the MPS target explicitly planned.
S[17]['title']='성장기 선수의 통합관리, <em>MPS가 넓혀갈 자리입니다</em>'
S[17]['sub']='각 분야의 전문성을 바이오밴딩 기반 기록으로 연결하고, 지역 제휴기관으로 확장합니다.'
S[17]['cls']='sector-comparison quadrant-comparison'
S[17]['body']='''<div class="competitive-graphic" role="img" aria-label="공개 서비스 중심을 해석한 개념도. 가로축은 일상 건강에서 선수와 경기 현장 중심, 세로축은 분야별 전문관리에서 성장 피지컬 멘탈 연계. MPS의 성장기 선수 통합관리 지향점은 예정입니다.">
<div class="q-y-top">성장 + 피지컬 + 멘탈 연계</div>
<div class="q-plane"><div class="q-region q-r1"></div><div class="q-region q-r2"></div><div class="q-region q-r3"></div><div class="q-region q-r4"></div><div class="q-axis-x"></div><div class="q-axis-y"></div>
<div class="q-node q-growth"><small>성장클리닉</small><b>함소아 <span>/</span> 하이키</b><p>성장 검사와 진료</p></div>
<div class="q-node q-mind"><small>멘탈센터</small><b>마인드카페</b><p>심리검사와 상담</p></div>
<div class="q-node q-rehab"><small>스포츠 재활</small><b>하늘병원 <span>/</span> 세종스포츠정형외과</b><p>손상 진료와 운동 복귀</p></div>
<div class="q-node q-physical"><small>피지컬센터</small><b>플코 <span>/</span> 솔리드</b><p>선수 측정과 훈련</p></div>
<div class="q-mps"><small>10–15세 선수 통합관리 / 지향점 (예정)</small><b>MPS</b><p>바이오밴딩 기반 리포트<br>기능평가 + 인지검사 + 성장 추적</p></div>
<div class="q-space">선수 한 명의 기록으로<br><b>전문 서비스를 연결</b></div>
</div><span class="q-x-left">일상 건강 중심</span><span class="q-x-right">선수와 경기 현장 중심 →</span><span class="q-y-bottom">분야별 전문관리</span>
</div><div class="graphic-scale"><div class="scale-lead"><small>전국 확장 설계</small><b>공통 기준을 지역으로</b></div><div class="scale-step"><i>01</i><span><b>본사 리포트와 교육</b><small>측정 기준과 품질관리</small></span></div><em>→</em><div class="scale-step"><i>02</i><span><b>지역 전문기관</b><small>의료기관 × 스튜디오 × 멘토</small></span></div><em>→</em><div class="scale-step"><i>03</i><span><b>월 계약과 재측정</b><small>반복 매출과 누적 기록</small></span></div></div>'''
S[17]['source']='공개 서비스 중심에 대한 정성적 배치 | MPS 위치는 지향점, 전국 제휴 확장 예정<br>'+' / '.join(link(url,name) for name,url in comparison_sources)
S[17]['notes']+='\n그래픽 해석: 가로축은 일상 건강관리에서 선수와 경기 현장 관리로의 초점, 세로축은 분야별 전문관리에서 성장/피지컬/멘탈을 함께 연결하는 관리로의 초점이다. 경쟁 기관은 앞서 확인한 공개 서비스 중심을 정성적으로 묶어 표시했으며 점수, 우열, 기능 부재, 시장점유율이나 실측 좌표가 아니다. 같은 분야의 두 기관이 동일 기능을 모두 제공한다는 뜻도 아니다. 플코는 측정과 훈련 및 앱 관리, 솔리드는 선수 훈련과 재활 트레이닝을 공개한다. MPS의 강조 영역은 향후 지향점으로 현재 검증된 통합 플랫폼 성과를 의미하지 않는다. 노드 크기는 매출, 고객 수 또는 시장 규모를 뜻하지 않는다.'
REFERENCE_CSS+='''
.quadrant-comparison .content{top:229px}
.competitive-graphic{height:441px;position:relative}
.q-y-top{position:absolute;top:0;left:560px;width:400px;text-align:center;font-size:17px;font-weight:700;color:#67686f}
.q-plane{position:absolute;left:25px;right:0;top:39px;height:340px}
.q-region{position:absolute;width:50%;height:50%;background:#fafafa}
.q-r1{top:0;left:0;border-top-left-radius:25px}.q-r2{top:0;right:0;background:#faf7f4;border-top-right-radius:25px}
.q-r3{bottom:0;left:0;background:#f7f7f9;border-bottom-left-radius:25px}.q-r4{bottom:0;right:0;background:#f6f4f9;border-bottom-right-radius:25px}
.q-axis-x{position:absolute;top:50%;left:0;right:0;border-top:1px dashed #c7c6cc}
.q-axis-y{position:absolute;left:50%;top:0;bottom:0;border-left:1px dashed #c7c6cc}
.q-axis-y:before{content:'↑';position:absolute;top:-25px;left:-7px;font-size:22px;color:#aaa7b2}
.q-node{position:absolute;border:1px solid #e1dce9;border-radius:18px;background:white;padding:12px 18px;box-shadow:0 3px 12px #20212604}
.q-node small{font-size:13px;color:#8874b8;display:block;margin-bottom:5px}
.q-node b{font-size:21px;white-space:nowrap}.q-node b span{font-weight:400;color:#b4b0bb;margin:0 5px}
.q-node p{font-size:15px;line-height:1.4;color:#77747e;margin-top:5px}
.q-growth{left:45px;top:219px;width:270px}
.q-mind{left:340px;top:188px;width:275px}
.q-rehab{left:780px;top:228px;width:375px}.q-rehab b{font-size:18px}
.q-physical{left:1165px;top:136px;width:270px}
.q-mps{position:absolute;top:15px;left:800px;width:320px;padding:15px 22px;border:1.5px dashed #fc582b;border-radius:24px;background:#fff0e6}
.q-mps small{display:block;font-size:12px;color:#a05a40}.q-mps>b{font-size:45px;line-height:1.25;display:block;color:#fc582b;margin:3px 0}
.q-mps p{font-size:16px;line-height:1.5;color:#514945}
.q-space{position:absolute;left:80px;top:43px;font-size:22px;line-height:1.7;color:#99959e}.q-space b{font-size:26px;color:#77717f}
.q-x-left,.q-x-right,.q-y-bottom{position:absolute;font-size:16px;color:#77747e;top:393px}
.q-x-left{left:30px}.q-x-right{right:0}.q-y-bottom{left:620px;width:250px;text-align:center}
.graphic-scale{display:flex;align-items:center;gap:23px;background:#f6f6f8;border-radius:20px;padding:22px 25px;margin-top:7px}
.scale-lead{width:270px;border-right:1px solid #dcdbe2;padding-right:20px}
.scale-lead small{display:block;color:#8874b8;font-size:14px;margin-bottom:8px}.scale-lead>b{font-size:23px}
.scale-step{display:flex;align-items:center;gap:12px;flex:1}.scale-step>i{font-style:normal;background:#ece7f3;color:#8874b8;border-radius:50%;width:32px;height:32px;display:flex;align-items:center;justify-content:center;font-size:14px;flex-shrink:0}
.scale-step b{font-size:20px;display:block;white-space:nowrap}.scale-step small{display:block;font-size:14px;color:#77747e;margin-top:9px;white-space:nowrap}
.graphic-scale>em{font-size:25px}
'''
(DOC/'경쟁서비스_비교근거_20260923.md').write_text('# 17페이지 그래픽 비교 근거\n\n'+'\n'.join('- ['+name+']('+url+')' for name,url in comparison_sources)+'\n\n'+S[17]['notes'])

# Page 17: spacious circular positioning diagram, presentation-only footer removed.
S[17]['title']='성장기 선수의 통합관리, <em>MPS의 차별점입니다</em>'
S[17]['sub']=''
S[17]['cls']='circle-positioning'
S[17]['source']=''
S[17]['body']='''<div class="circle-map" role="img" aria-label="서비스 초점을 비교하는 개념도. 일상 건강과 선수 관리, 전문 분야와 통합관리의 두 축. MPS는 바이오밴딩 기반 통합관리를 지향합니다.">
<div class="circle-axis horizontal"></div><div class="circle-axis vertical"></div>
<span class="circle-axis-label top">통합관리</span><span class="circle-axis-label bottom">전문 분야 중심</span><span class="circle-axis-label left">일상 건강</span><span class="circle-axis-label right">선수 관리</span>
<div class="peer-circle growth-circle"><small>성장클리닉</small><b>함소아<br>하이키</b><span>키 성장</span></div>
<div class="peer-circle mind-circle"><small>멘탈센터</small><b>마인드카페</b><span>심리상담</span></div>
<div class="peer-circle rehab-circle"><small>스포츠 재활</small><b>하늘병원<br>세종스포츠정형외과</b><span>치료와 복귀</span></div>
<div class="peer-circle plco-circle"><small>피지컬 관리</small><b>플코</b><span>측정과 훈련</span></div>
<div class="mps-circle"><small>10–15세 성장기 선수</small><b>MPS</b><strong>바이오밴딩</strong><span>성장 × 피지컬 × 멘탈</span><em>통합관리 지향</em></div>
<div class="circle-keywords"><span>성장단계</span><i>+</i><span>기능평가</span><i>+</i><span>인지검사</span></div>
</div>'''
S[17]['notes']+='\n최종 표현: 사용자 요청에 따라 솔리드, 하단 출처/브랜드, 전국 확장 흐름도를 발표 화면에서 제거했다. 출처와 비교 해석 근거는 이 발표자 노트와 별도 근거 문서에 보존한다. 원의 위치와 크기는 서비스 초점을 설명하는 개념 표현이며 정량 점수나 시장 규모가 아니다. 성장클리닉은 키 성장, 멘탈센터는 심리상담, 스포츠 재활은 치료와 복귀, 플코는 측정과 훈련을 대표 키워드로 선택했다. 이는 각 기관의 전체 서비스를 제한하는 설명이 아니다. MPS는 통합관리 지향점으로 표시한다.'
REFERENCE_CSS+='''
.circle-positioning .heading{margin-top:23px}
.circle-positioning .content{top:204px;bottom:46px}
.circle-positioning footer{display:none}
.circle-map{position:relative;width:1480px;height:640px}
.circle-axis{position:absolute;background:#dedde3}
.circle-axis.horizontal{left:30px;right:30px;top:286px;height:1px}
.circle-axis.vertical{left:720px;top:44px;bottom:35px;width:1px}
.circle-axis.horizontal:after{content:'';position:absolute;right:0;top:-3px;width:7px;height:7px;border-top:1px solid #b8b5bf;border-right:1px solid #b8b5bf;transform:rotate(45deg)}
.circle-axis.vertical:before{content:'';position:absolute;left:-3px;top:0;width:7px;height:7px;border-top:1px solid #b8b5bf;border-left:1px solid #b8b5bf;transform:rotate(45deg)}
.circle-axis-label{position:absolute;color:#85818d;font-size:18px;letter-spacing:.2px;background:#fff;padding:0 12px}
.circle-axis-label.top{top:8px;left:655px;width:130px;text-align:center}
.circle-axis-label.bottom{bottom:3px;left:620px;width:200px;text-align:center}
.circle-axis-label.left{top:253px;left:17px}.circle-axis-label.right{top:253px;right:18px}
.peer-circle{position:absolute;display:flex;align-items:center;justify-content:center;flex-direction:column;text-align:center;border-radius:50%;background:#f6f5f8;border:1px solid #e8e5ee;width:176px;height:176px}
.peer-circle small{font-size:13px;color:#91869f;margin-bottom:10px}
.peer-circle b{font-size:23px;line-height:1.4;color:#46424d;font-weight:700}
.peer-circle>span{font-size:15px;color:#8a8493;margin-top:12px}
.growth-circle{left:170px;top:366px}.mind-circle{left:411px;top:323px}
.rehab-circle{left:835px;top:367px;width:202px;height:202px}.rehab-circle b{font-size:18px;line-height:1.5}
.plco-circle{left:1156px;top:305px}
.mps-circle{position:absolute;left:933px;top:2px;width:250px;height:250px;border-radius:50%;border:1.5px solid #fc582b;background:#fff2eb;display:flex;align-items:center;justify-content:center;flex-direction:column;box-shadow:0 0 0 14px #fffaf7}
.mps-circle small{font-size:13px;color:#936b5b;margin-bottom:5px}.mps-circle>b{font-size:58px;line-height:1.2;letter-spacing:-1px;color:#fc582b}
.mps-circle strong{font-size:22px;color:#4b3d38;margin-top:4px}.mps-circle>span{font-size:16px;color:#79655d;margin-top:9px}
.mps-circle em{font-size:12px;color:#a08b82;margin-top:9px}
.circle-keywords{position:absolute;top:112px;left:1240px;display:grid;grid-template-columns:1fr;text-align:center;gap:5px;color:#8874b8;font-size:17px}
.circle-keywords i{font-style:normal;color:#c2b8cd;font-size:13px}
'''
(DOC/'경쟁서비스_비교근거_20260923.md').write_text('# 17페이지 비교 근거\n\n화면은 원형 개념도로 간소화. 자료 출처는 발표자 노트에 보존.\n\n'+S[17]['notes'])

# Mental service definition: assessment followed by mentoring.
S[2]['sub']='멘탈평가와 멘토링, 피지컬 기능평가와 강화를 바이오밴딩 기반 성장관리로 연결합니다.'
S[2]['body']=S[2]['body'].replace('바이오밴딩 + 인지검사','스포츠심리 + 인지발달검사').replace('멘탈 멘토링</b>','멘탈평가와 멘토링</b>')
S[3]['body']=S[3]['body'].replace('측정과 상담이 필요한 성장기','측정과 지원이 필요한 성장기')
S[6]['body']=S[6]['body'].replace('바이오밴딩 + 인지검사','스포츠심리 + 인지발달검사')
S[7]=service('해결 방법 / M 멘탈평가',
 '스포츠심리와 인지발달을 평가해, <em>멘탈멘토링으로 연결합니다</em>',
 '스포츠심리검사와 인지발달검사 등으로 강점과 과제를 파악하고, 바이오밴딩 맥락에서 멘토링 방향을 정합니다.',
 'mental-2.png','mental-focus.png','평가 결과를 멘토링의 출발점으로',
 '멘탈평가 후<br><em>멘탈멘토링.</em>',
 ['스포츠심리검사와 인지발달검사','선수의 강점과 과제를 리포트로','평가 결과에 맞춘 멘토링 계획'],
 ['멘탈평가','리포트 해석','멘탈멘토링'],
 '멘탈평가 이용료 → 멘탈멘토링 프로그램',
 'MPS의 멘탈 서비스는 스포츠심리검사와 인지발달검사 등을 통한 멘탈평가 후 멘탈멘토링을 제공하는 모델이다. 바이오밴딩은 성장단계를 함께 이해하는 해석 맥락이다. 선수의 강점과 과제를 리포트로 정리하고 프로선수 출신 멘토가 이를 멘토링에 활용한다. 심리치료 또는 일반 심리상담 프로그램으로 설명하지 않는다. 사용자가 유럽 프로팀 수준의 검사라고 설명했으나 구체적인 검사명과 적용 팀 및 기관 근거가 제공되기 전에는 검증된 동등성이나 정확도를 발표 문구로 단정하지 않는다. 리포트 이미지는 가상 선수 예시이며 실제 검사 항목과 도구 매핑은 제품 고도화 과정에서 정리한다.')
S[7]['no']=8
S[8]['sub']='멘탈평가 후, 매일 또는 격일의 다이어리를 바탕으로 프로선수 출신 멘토가 멘탈멘토링을 진행합니다.'
S[8]['body']=S[8]['body'].replace('프로선수 출신 멘토(심리상담사)가 확인','프로선수 출신 멘토가 기록 확인').replace('일상의 기록을 바탕으로 개별 멘토링','멘탈평가와 일상 기록으로 멘토링').replace('멘탈 멘토와 선수의 상담 이미지','멘탈 멘토와 선수의 멘토링 이미지')
S[8]['notes']='스포츠심리검사, 인지발달검사 등을 통한 멘탈평가를 먼저 실시하고 그 결과와 일상의 기록을 멘탈멘토링으로 연결한다. 프로선수 출신 멘토는 심리상담사 자격을 가진 인력으로 사용자에게 소개되었지만 제공 서비스는 멘탈멘토링이다. 선수는 매일 또는 격일로 멘탈 다이어리를 기록하고 멘토가 이를 확인해 개별 멘토링과 변화 리뷰를 진행한다. 기록 주기가 멘토의 응답시간 보장을 의미하지 않는다. 모바일앱은 출시 예정이며 서비스 운영은 고도화 중이다. 리포트는 가상 선수 샘플이다.'
S[17]['body']=S[17]['body'].replace('<em>통합관리 지향</em>','<em>통합관리 지향</em>').replace('<span>인지검사</span>','<span>멘탈평가</span>').replace('</div>\n<div class="circle-keywords">','</div>\n<div class="circle-keywords">')
S[17]['body']=S[17]['body'].replace('<span>성장 × 피지컬 × 멘탈</span>','<span>성장 × 피지컬 × 멘탈</span><div class="circle-mental">멘탈평가 → 멘탈멘토링</div>')
S[17]['body']=S[17]['body'].replace('<span>멘탈평가</span></div>','<span>스포츠심리검사</span><i>+</i><span>인지발달검사</span></div>')
S[18]['body']=S[18]['body'].replace('바이오밴딩 + 인지검사 기반','스포츠심리검사 + 인지발달검사').replace('의료기관, 프로선수 출신 멘토, 스튜디오','의료기관, 멘탈멘토링, 스튜디오')
S[18]['sub']='바이오밴딩 기반으로 멘탈평가 후 멘탈멘토링, 기능평가 후 컨디셔닝을 연결합니다.'
S[23]['body']=S[23]['body'].replace('현장 / 상담','현장 / 멘토링').replace('운영 / 상담','운영 / 지원').replace('교육 상담 총괄','교육 멘토링 운영')
S[25]['sub']=S[25]['sub'].replace('리포트 상담','리포트 해석')
# Remove earlier explanatory history that mislabels the mental product.
for i in [2,6,17,18,23,25,26]:
 S[i]['notes']=S[i]['notes'].replace('인지검사','인지발달검사').replace('본사 상담','멘탈멘토링').replace('평가–상담','평가–멘토링').replace('리포트 상담','리포트 해석')
S[2]['notes']+='\n최신 멘탈 서비스 정의: 스포츠심리검사와 인지발달검사 등을 통한 멘탈평가 → 멘탈멘토링.'
S[17]['notes']+='\nMPS의 멘탈 차별점은 스포츠심리검사 및 인지발달검사 등을 통한 멘탈평가 후 프로선수 출신 멘토의 멘탈멘토링으로 연결하는 것이다. 마인드카페의 심리상담 표기는 해당 경쟁기관 서비스에 관한 설명으로 유지했다.'
REFERENCE_CSS+='''
.circle-mental{font-size:14px;color:#a65135;font-weight:700;margin-top:8px}
.circle-positioning .mps-circle em{margin-top:6px;font-size:11px}
.circle-positioning .mps-circle>b{font-size:52px}
.circle-positioning .circle-keywords{top:94px;font-size:15px;left:1230px}
'''
(DOC/'멘탈서비스_정의.md').write_text('# MPS 멘탈 서비스\n\n스포츠심리검사 + 인지발달검사 등 → 멘탈평가 리포트 → 멘탈멘토링 → 일상 기록과 리뷰.\n\n프로선수 출신 멘토가 평가 결과와 다이어리를 바탕으로 멘토링한다. 모바일앱은 출시 예정.\n\n대표 설명: 유럽 프로팀 수준의 검사. 외부 발표 비교 근거에 사용할 검사명과 적용 팀/기관 확인 대기.\n')

# Founder identifies PCDEQ as the basis of mental assessment.
PCDEQ_RESEARCH='https://pubmed.ncbi.nlm.nih.gov/31607218/'
PCDEQ_ORIGINAL='https://pubmed.ncbi.nlm.nih.gov/21812724/'
S[7]['title']='PCDEQ 기반 멘탈평가, <em>선수의 멘탈멘토링으로 이어집니다</em>'
S[7]['sub']='선수 발달의 심리적 특성을 평가하고, 인지발달검사와 성장단계 해석을 더해 멘토링 방향을 정합니다.'
S[7]['body']=S[7]['body'].replace('스포츠심리검사와 인지발달검사','PCDEQ 기반 스포츠심리평가').replace('선수의 강점과 과제를 리포트로','인지발달검사로 이해를 보완').replace('평가 결과에 맞춘 멘토링 계획','강점과 과제에 맞춘 멘토링 계획').replace('멘탈평가 후<br>','PCDEQ 기반 평가 후<br>')
S[7]['source']=link(PCDEQ_RESEARCH,'잉글랜드 프로 아카데미 11–16세 선수 대상 PCDEQ 연구')+' | 가상 리포트 샘플 / MPS 적용 고도화 중'
S[7]['notes']='MPS는 PCDEQ 기반 멘탈평가 후 멘탈멘토링을 제공한다는 대표 설명을 반영했다. PCDEQ의 정식 명칭은 Psychological Characteristics of Developing Excellence Questionnaire이며 선수 발달에 필요한 심리적 특성을 평가하는 질문지다. 인지발달검사는 별도 구성요소로 제시하며 PCDEQ 자체를 인지발달검사로 설명하지 않는다. 평가 결과, 바이오밴딩의 성장 맥락, 일상 기록을 프로선수 출신 멘토의 멘탈멘토링에 활용한다. 실제 MPS 검사 버전, 번안 문항, 점수 산식 및 인지발달검사 도구는 별도 확인 대상이다. 리포트 샘플의 척도를 원 PCDEQ의 검증된 척도와 동일하다고 단정하지 않는다.\nSaward 등 연구는 잉글랜드 프로 아카데미의 11–16세 선수111명에게 PCDEQ를 적용했다. 연구에서의 사용은 모든 프로팀의 표준 운영 또는 MPS 서비스와 동등한 성능을 입증하는 의미가 아니다. 대표가 제시한 비교 국가에는 잉글랜드, 네덜란드, 벨기에가 포함된다. 이번 장표에서는 확인한 잉글랜드 연구를 근거로 사용했다.\n원 도구 개발 연구: '+PCDEQ_ORIGINAL+'\n아카데미 선수 연구: '+PCDEQ_RESEARCH
for i in [2,6]:
 S[i]['body']=S[i]['body'].replace('스포츠심리 + 인지발달검사','PCDEQ + 인지발달검사')
 S[i]['notes']+='\n멘탈평가는 대표 설명에 따라 PCDEQ 기반으로 표기. 인지발달검사는 별도 구성요소. PCDEQ 연구: '+PCDEQ_RESEARCH
S[8]['sub']='PCDEQ 기반 멘탈평가 후, 매일 또는 격일의 다이어리를 바탕으로 프로선수 출신 멘토가 멘탈멘토링을 진행합니다.'
S[8]['notes']='PCDEQ 기반 멘탈평가와 별도 인지발달검사 등의 결과를 멘탈멘토링으로 연결한다. '+S[8]['notes']
S[17]['body']=S[17]['body'].replace('<span>스포츠심리검사</span>','<span>PCDEQ 멘탈평가</span>')
S[17]['notes']+='\nPCDEQ 기반 스포츠심리평가와 인지발달검사를 분리해 표기했다. 확인 연구: '+PCDEQ_RESEARCH
S[18]['body']=S[18]['body'].replace('스포츠심리검사 + 인지발달검사','PCDEQ 기반 평가 + 인지발달검사')
S[18]['notes']+='\nMPS의 멘탈평가는 PCDEQ 기반이라는 대표 설명을 반영했다. 인지발달검사는 별도 항목이다.'
(DOC/'멘탈서비스_정의.md').write_text('# MPS 멘탈 서비스\n\nPCDEQ 기반 멘탈평가 + 별도 인지발달검사 → 리포트 해석 → 멘탈멘토링 → 일상 기록과 리뷰. 바이오밴딩은 성장단계 해석 맥락.\n\nPCDEQ: Psychological Characteristics of Developing Excellence Questionnaire. 선수 발달의 심리적 특성을 평가하는 질문지.\n\n대표 제공 비교 대상: 잉글랜드, 네덜란드, 벨기에 프로산하팀. 확인된 연구는 잉글랜드 프로 아카데미 선수 대상 연구이며, 국가별 전체 채택 또는 MPS와의 성능 동등성을 의미하지 않는다.\n\n- [원 도구 개발 연구]('+PCDEQ_ORIGINAL+')\n- [잉글랜드 프로 아카데미 선수 연구]('+PCDEQ_RESEARCH+')\n\n'+S[7]['notes'])
(DOC/'경쟁서비스_비교근거_20260923.md').write_text('# 17페이지 비교 근거\n\n'+S[17]['notes'])

# Printed page 18: MPS brand hierarchy in the direct comparison.
S[18]['cls']='plco-brand-comparison'
S[18]['title']='플코(PLCO)와 MPS, <em>성장단계부터 관리가 달라집니다</em>'
S[18]['body']=table(['비교 기준','<span class="compare-brand">PLCO</span><small>공개 서비스</small>','<span class="compare-brand">SPORTS MPS</span><small>10–15세 성장기 선수 통합관리</small>'],[
 ['대상','유소년 및 엘리트 팀','<strong>10–15세 성장기 선수</strong>'],
 ['피지컬','피지컬 측정, 리포트, 훈련','<strong>바이오밴딩</strong><span class="compare-plus"> + </span><b>기능평가</b>'],
 ['멘탈','공개 서비스 범위 참고','<strong>PCDEQ 기반 멘탈평가</strong><small>인지발달검사 + 멘탈멘토링</small>'],
 ['후속 서비스','앱, 웹, 오프라인 짐','<b>의료기관 × 스튜디오 × 멘탈멘토링</b><small>성장단계 기반 측정 → 강화 → 재측정</small>']])
REFERENCE_CSS+='''
.plco-brand-comparison .content{top:251px}
.plco-brand-comparison table{table-layout:fixed;border-collapse:separate;border-spacing:0}
.plco-brand-comparison th{padding:21px 25px;background:#f2f2f4;color:#74747d;font-size:17px;vertical-align:middle}
.plco-brand-comparison th:first-child{width:13%;background:#fff;color:#77717f}
.plco-brand-comparison th:nth-child(2){width:32%;border-top-left-radius:16px}
.plco-brand-comparison th:last-child{width:55%;background:#fc582b;color:white;border-radius:16px 16px 0 0;padding-left:32px}
.plco-brand-comparison .compare-brand{display:block;font-size:25px;font-weight:700;line-height:1.1}
.plco-brand-comparison th:last-child .compare-brand{font-size:36px;font-weight:800;letter-spacing:-.7px}
.plco-brand-comparison th small{display:block;margin-top:9px;font-size:14px;font-weight:400}
.plco-brand-comparison th:last-child small{font-size:17px;color:#fff}
.plco-brand-comparison td{padding:20px 25px;vertical-align:middle;border-bottom:1px solid #e7e5e9;background:#fff;line-height:1.4}
.plco-brand-comparison td:first-child{font-size:18px;font-weight:500;color:#77717f}
.plco-brand-comparison td:nth-child(2){font-size:21px;color:#777780;background:#fafafa}
.plco-brand-comparison td:last-child{padding-left:32px;background:#fff4ed;font-size:27px;color:#29262d;border-bottom:1px solid #eedfd5}
.plco-brand-comparison td strong{color:#e94c23;font-weight:800}
.plco-brand-comparison td b{font-weight:700}
.plco-brand-comparison td small{display:block;font-size:20px;color:#8874b8;margin-top:9px;font-weight:500}
.plco-brand-comparison .compare-plus{color:#a6a0ad;font-weight:400}
.plco-brand-comparison tr:last-child td:last-child{border-radius:0 0 16px 16px;font-size:25px}
.plco-brand-comparison tr:last-child td:nth-child(2){border-bottom-left-radius:16px}
'''

# Subtle emphasis: balanced comparison with restrained MPS accents.
S[18]['title']='플코(PLCO)와 MPS, <em>성장관리의 초점이 다릅니다</em>'
REFERENCE_CSS+='''
.plco-brand-comparison th{background:#f5f5f7;color:#55535c;padding:22px 25px}
.plco-brand-comparison th:nth-child(2){width:39%;border-top:2px solid #e4e2e8;border-top-left-radius:10px}
.plco-brand-comparison th:last-child{width:48%;background:#f5f5f7;color:#29262d;border-top:2px solid #fc582b;border-radius:10px 10px 0 0;padding-left:28px}
.plco-brand-comparison .compare-brand,.plco-brand-comparison th:last-child .compare-brand{font-size:26px;font-weight:700;letter-spacing:0}
.plco-brand-comparison th small,.plco-brand-comparison th:last-child small{font-size:14px;color:#77747e;font-weight:400}
.plco-brand-comparison td{padding:21px 25px}
.plco-brand-comparison td:nth-child(2){font-size:22px;color:#66636d;background:#fff}
.plco-brand-comparison td:last-child{padding-left:28px;background:#fff;font-size:23px;color:#38343e;border-bottom:1px solid #e7e5e9}
.plco-brand-comparison td strong{color:#38343e;font-weight:600}
.plco-brand-comparison td b{font-weight:600}
.plco-brand-comparison tbody tr:nth-child(2) td:last-child strong{color:#d95733}
.plco-brand-comparison tbody tr:nth-child(3) td:last-child strong{color:#8874b8}
.plco-brand-comparison td small{font-size:18px;color:#77747e;margin-top:8px;font-weight:400}
.plco-brand-comparison tr:last-child td:last-child{font-size:22px;border-radius:0}
.plco-brand-comparison td:first-child{color:#77747e}
'''

# Founder wording correction: keep PCDEQ in supporting notes only.
for r in S:
 for key in ['title','sub','body','source']:
  r[key]=r[key].replace('PCDEQ 기반 스포츠심리평가','스포츠심리평가 + 인지검사').replace('PCDEQ 기반 멘탈평가','멘탈').replace('PCDEQ 기반 평가','멘탈평가').replace('PCDEQ 멘탈평가','스포츠심리평가').replace('PCDEQ + 인지발달검사','스포츠심리평가 + 인지검사').replace('인지발달검사','인지검사')
S[7]['title']='멘탈은 <em>바이오밴딩 + 스포츠심리평가 + 인지검사 기반입니다</em>'
S[7]['sub']='스포츠심리평가와 인지검사로 강점과 과제를 파악하고, 성장단계를 함께 보며 멘탈멘토링으로 연결합니다.'
S[7]['body']=S[7]['body'].replace('멘탈평가 후<br><em>멘탈멘토링.</em>','멘탈을 이해하고<br><em>멘탈멘토링으로.</em>').replace('인지검사로 이해를 보완','성장단계와 함께 결과 해석')
S[7]['source']='가상 선수의 예시 데이터 | 리포트와 프로그램 고도화 중'
S[8]['sub']='멘탈평가 후, 매일 또는 격일의 다이어리를 바탕으로 프로선수 출신 멘토가 멘탈멘토링을 진행합니다.'
S[17]['body']=S[17]['body'].replace('<span>스포츠심리검사</span>','<span>스포츠심리평가</span>')
S[18]['body']=S[18]['body'].replace('<strong>멘탈</strong><small>인지검사 + 멘탈멘토링</small>','<strong>멘탈</strong><small>스포츠심리평가 + 인지검사</small>')
# Keep the longer summary label readable within its original card.
REFERENCE_CSS+='''
.summary-mps article:last-child{min-width:0}
'''
for i in [2,6,7,8,17,18]:
 S[i]['notes']+='\n발표 화면 최종 용어: 멘탈 / 스포츠심리평가 + 인지검사 / 멘탈멘토링. PCDEQ는 도구 기반 설명으로 근거 문서와 노트에만 보존한다.'

# Exact founder wording for the mental assessment basis.
mental_basis='바이오밴딩 + 스포츠심리평가/인지검사'
S[7]['title']='멘탈은 <em>'+mental_basis+' 기반입니다</em>'
S[18]['body']=S[18]['body'].replace('<small>스포츠심리평가 + 인지검사</small>','<small>'+mental_basis+'</small>')
S[6]['body']=S[6]['body'].replace('스포츠심리평가 + 인지검사',mental_basis)
S[2]['body']=S[2]['body'].replace('스포츠심리평가 + 인지검사',mental_basis)
S[17]['body']=S[17]['body'].replace('<span>스포츠심리평가</span><i>+</i><span>인지검사</span>','<span>스포츠심리평가/인지검사</span>')
for i in [2,6,7,17,18]:S[i]['notes']+='\n멘탈 평가 기반 최종 표기: '+mental_basis+'.'
REFERENCE_CSS+='''
.plco-brand-comparison tbody tr:nth-child(3) td:last-child small{font-size:18px}
.circle-positioning .circle-keywords{left:1220px;font-size:14px}
'''
S[2]['body']=S[2]['body'].replace(mental_basis,'바이오밴딩 +<br>스포츠심리평가/인지검사')
REFERENCE_CSS+='''
.summary-domains .domain-m .domain-basis{white-space:normal;font-size:12.5px;line-height:1.12;margin-top:6px;padding-top:5px}
'''

# Insert after all existing indexed edits: founder precedes the team slide.
founder_photo=ROOT/'20260919 사업제안서/사진자료/스태프/이정욱_캐주얼_상반신.png'
founder_panels=[
 ('01 / 임상과 교육','20년의 전문성','3대째 한의사, 스포츠한의학 20년<br>동국대와 가천대 한의학과 겸임교수<br>메디스트림 강의, 헬릭스미스 자문'),
 ('02 / 축구의학','선수 곁의 팀닥터','FIFA 축구의학 코스 수료<br>스포츠한의학회 공인 팀닥터<br>서울 대동초 축구부 팀닥터'),
 ('03 / 현장과 교류','국내외 축구 현장 경험','J리그 팀 등 한일 교류와 대회 의무지원<br>슛포러브 프로그램 촬영 지원<br>스포츠 심리상담사 1급'),
 ('04 / 부모와 지도자','고객의 고민을 아는 대표','축구선수 학부모, 초등 축구부 학부모대표<br>클럽과 학교, 프로 산하와 골든에이지<br>선수 육성 과정을 직접 경험')]
founder_body='<div class="ceo-profile"><div class="ceo-portrait">'+pic(founder_photo,'이정욱 대표','ceo-person')+'<div class="ceo-name"><small>SPORTS MPS / 주니어골든에이지</small><h2>이정욱 <span>대표</span></h2><p>해온한의원 본원 대표 한의사</p></div></div><div class="ceo-evidence"><div class="ceo-four">'+''.join('<article><small>'+label+'</small><h3>'+title+'</h3><p>'+detail+'</p></article>' for label,title,detail in founder_panels)+'</div><div class="ceo-mission"><small>대표의 문제의식에서 시작한 MPS</small><strong>재능이 낙오되지 않는 세상.</strong><span>의료의 전문성, 축구 현장, 부모의 경험을 하나의 서비스로.</span></div></div></div>'
founder=dict(no=24,cat='대표 역량',title='대표 이정욱, <em>현장과 전문성을 잇습니다</em>',sub='의료와 교육, 축구 현장에서 쌓은 경험으로 선수의 성장관리를 사업으로 연결합니다.',body=founder_body,source='',cls='ceo-capability',notes='사용자가 지정한 기존 사업제안서 20260919 사업제안서/index.html의 대표 소개(표기20페이지)를 바탕으로 동일 인물 사진과 경력 내용을 구성했다. 20년의 임상과 교육: 3대째 한의사, 스포츠한의학20년, 동국대와 가천대 한의학과 겸임교수, 메디스트림 강의, 헬릭스미스 자문. 축구의학: FIFA 축구의학 코스 수료, 스포츠한의학회 공인 팀닥터, 서울 대동초 축구부 팀닥터. 현장: J리그 팀 등 한일교류 및 각종 대회 의무지원, 슛포러브 프로그램 촬영 지원, 스포츠 심리상담사1급. 부모 경험: 축구선수 학부모, 클럽/학교/프로산하/골든에이지 경험, 초등 축구부 학부모대표. 모두 사용자 제공 기존 소개자료 기준이며 새로운 성과나 계약을 추가하지 않았다. 자격과 경력은 멘탈평가 후 멘탈멘토링이라는 MPS 서비스 정의와 구분한다. 원자료 학력: 도쿄 石川台中学校, 서울 경기고, 동국대 한의학과. 원자료 수료증: FIFA Diploma in Football Medicine, 2020.08.11. 수료 이력을 학위로 표시하지 않는다. 원자료 미션: 재능이 낙오되지 않는 세상, 단정짓기보다 성장의 시간을 지켜줍니다.')
S.insert(23,founder)
for i,r in enumerate(S,1):r['no']=i
S[1]['body']=S[1]['body'].replace('팀원 소개','대표 역량과 팀원 소개').replace('<b>23</b>','<b>23–24</b>').replace('<b>24</b>','<b>25</b>').replace('<b>25–26</b>','<b>26–27</b>')
REFERENCE_CSS+='''
.ceo-capability .content{top:235px}
.ceo-profile{display:grid;grid-template-columns:365px 1fr;gap:40px;height:552px}
.ceo-portrait{position:relative;border-radius:22px;background:#f7f6f8;overflow:hidden}
.ceo-person{display:block;width:100%;height:397px;object-fit:contain;object-position:center bottom;padding:10px 12px 0}
.ceo-name{padding:19px 24px;background:#f7f6f8;border-top:1px solid #e7e4ea}
.ceo-name>small{font-size:12px;color:#8874b8}.ceo-name h2{font-size:35px;line-height:1.25;margin:10px 0 6px}.ceo-name h2 span{font-size:22px;font-weight:500;margin-left:7px}
.ceo-name p{font-size:17px;color:#67636d}
.ceo-four{display:grid;grid-template-columns:1fr 1fr;gap:19px 24px}
.ceo-four article{padding:22px 24px;border:1px solid #e7e5eb;border-radius:17px;background:#fff}
.ceo-four article>small{font-size:13px;color:#8874b8}.ceo-four h3{font-size:28px;margin:10px 0 13px;line-height:1.3}
.ceo-four p{font-size:18px;line-height:1.75;color:#625e68;letter-spacing:-.3px}
.ceo-mission{margin-top:23px;padding-left:23px;border-left:3px solid #fc582b;display:flex;flex-direction:column;gap:8px}
.ceo-mission small{font-size:13px;color:#8874b8}.ceo-mission strong{font-size:29px;line-height:1.3;color:#29262d}.ceo-mission span{font-size:18px;color:#67636d}
'''
(DOC/'대표역량_추가근거.md').write_text('# 대표 역량 장표\n\n표기23페이지에 추가, 기존 팀원 소개는24페이지로 이동.\n\n'+founder['notes'])
REFERENCE_CSS+='''
.ceo-four article{padding:18px 24px}
.ceo-mission{margin-top:19px}
'''

# Founder mission: specific reasons talent can be overlooked or lost.
founder_slide=next(r for r in S if r['cls']=='ceo-capability')
founder_slide['body']=founder_slide['body'].replace('<strong>재능이 낙오되지 않는 세상.</strong><span>의료의 전문성, 축구 현장, 부모의 경험을 하나의 서비스로.</span>','<strong class="ceo-mission-specific">멘탈의 어려움, 부상, 작은 체격이나 빠른 성숙 때문에<br><em>재능이 낙오되지 않도록.</em></strong>')
founder_slide['notes']+='\n대표 미션 최신 문구: 멘탈의 어려움, 부상, 작은 체격이나 빠른 성숙 때문에 재능이 낙오되지 않도록.'
REFERENCE_CSS+='''
.ceo-mission .ceo-mission-specific{font-size:25px;line-height:1.45;letter-spacing:-.5px}
'''
