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
