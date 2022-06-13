# Mock AvatarGen

Demonstration Purpose Mock Headless Dynamic Avatar Generation API Server.

## 시놉시스

- 사람 사진을 올리면, 동적으로 3D 모델 파일을 생성하는 시나리오를 시뮬레이션
- 간단한 데모를 위하여, `restclient/*.png` 파일을 전송하면,
  해당 파일명과 일치하는 `*.glb` 파일을 `data/mpar/` 폴더에서 찾아
  마치 동적으로 생성된 것처럼 다운로드 함.
- 전송 이미지 파일명과 매핑되는 `*.glb` 파일이 발견되지 않으면 에러 리턴.

## 설치

- Python 3 설치
- Flask 설치

```
> pip install flask
...
...
> flask --version
Python 3.9.6
Flask 2.1.2
Werkzeug 2.1.2
...
```

- Microsoft 3D Viewer 설치

아래 URL을 통해 설치:

  -- https://apps.microsoft.com/store/detail/3d-viewer/9NBLGGH42THS

위 앱을 설치하면, 탐색기에서 `*.glb` 파일을 더블클릭만 해도 3D 모델을 직접 볼 수 있음.

## 서버 실행

- `demo/mockavatar` 디렉토리로 이동하여 아래 명령 실행
```
> flask run
```

- 위의 명령은 기본적으로 http://localhost:5000 에 서버를 시작함.
- 위 서버가 제공하는 REST API는 `/api/my_avatar/v1/generate` 하나로,
  `POST` 메소드로 이미지 파일 하나를 클라이언트가 전송하면,
  동일한 파일명의 `.glb` 파일을 `data/mpar/` 폴더에서 찾아서 다운로드 함.
- `.glb` 파일이 발견되지 않으면, 404 에러.

## 테스트

아래 `curl` 명령들을 실행하여, `.png` 입력 파일을 통해, `.glb` 출력 파일 다운로드 테스트

```
> cd demo\mockavatar
> 
> curl -v -F style=classic -F file=@restclient/scarlett_johansson.png -o output1.glb http://localhost:5000/api/my_avatar/v1/generate
>
> dir *.glb
...

> curl -v -F style=classic -F file=@restclient/roman_reigns.png -o output2.glb http://localhost:5000/api/my_avatar/v1/generate
> dir *.glb
...
```

다운로드 된 `.glb` 파일을 Microsoft 3D Viewer와 같은 도구로 열어 확인하기.

또는 `restclient/test.http` 에 있는 두 가지 POST 요청 호출하여, `.glb` 파일 다운로드 테스트
(단, 이 경우 Visual Studio Code에서 바이너리 출력을 에디터 UI에 표시하느라 속도 저하됨)
