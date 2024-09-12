## Python 3.11+ 이상의 버전 설치 

## virtualenv 구성 
<code>
  python3 -m pip install --user -U virtualenv 
</code>

## virtual env 활성화하기 
<code>
  virtualenv kabang  
  .\kabang\Scripts\activate 
</code>

## 관련 코드 내려 받기 
1. 샘플을 사용할 폴더를 지정하고
<code>
  git clone https://github.com/javaos74/kabang-chainlit  mydemo 
</code>

## 필요한 패키지 설치하기 
<code>
  cd mydemo 
  pip install -r requirements.txt 
</code>

## 환경변수 구성하기 
.env 파일을 생성하고 아래와 같은 값을 채워준다. 
<code>
OPENAI_API_KEY=sk-로 시작하는 OpenAI api key 
#UiPath orchestrator information 
#for uipath orchestrator 
USER_NAME=test # 무시해도 됨
PASSWORD=test # 무시해도 됨 
ORCHESTRATOR_URL=https://cloud.uipath.com   # 실제 내부 automation suite cluster domain 
ORG_NAME=myrobkdybrlj
TENANT_NAME=charles
CLIENT_ID=xxxxx # 관리자 > 설정 > 외부 어플리케이션 에서 기밀 어플리케이션 추가, 어플리케이션 범위 선택 , Folder, Queue 관련 write 권한 추가 후 생성된 클라이언트 ID
CLIENT_SECRET=yyyyy #클라이언트 시크릿
SCOPE=  #외부 어플리케이션 만들때 사용한 범위 값인데 공백으로 유지 
</code>

## 내부 거래 내역서 DB 
kabang.db (SQLite3) 파일에 관련 내용 있음. 필요시 추가 
localdb.sql 에 관련 스키마 및 샘플 script 있음 
transactiondb.py 파일에 해당 kabang.db를 읽어 로그인과 거래내역서 요청 리스트를 확인 함 

## UiPath process 호출 
uipathlib.py 파일을 이용해서 .env 에 설정된 정보로 인증을 처리하고 지징된 폴더 (매뉴얼로 지정)와 queue에 데이터 추가 후 자동으로 프로세스가 호출(큐 트리거)되고 실행되기를 기다렸다가 결과를  queue의 Output에 지정함 
이 값을 읽어서 LLM 에 전달 함 
실제 프로세스와 큐 트리거 구성은 Orchestrator에서 구성을 해줘야 함 
큐에 추가되는 데이터의 입력(SpecificContent)에 값을 코드에서 사전에 지정해야 함 
동일한 큐를 사용하는 경우를 고려해서 프로세스 식별자는 반드시 Reference를 사용해야 함 (우체국 등기조회는 PostOffice를 값으로 사용 함)

## 실행 방법 
<code>
  chainlit run app.py -w 
  기본 브라우저가 열리고 127.0.0.1:8080 으로 연결을 시도함 
</code>
