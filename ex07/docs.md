## Linux 컨테이너를 Linux, Windows 또는 Mac에서 실행할 때의 차이점
Docker는 컨테이너를 생성, 관리, 관리하고 오케스트레이션하는 소프트웨어로, Linux와 Windows 모두에서 실행됩니다. Docker는 동일한 CLI(명령줄 인터페이스), API, 이미지 형식, 콘텐츠 배포 서비스를 사용하므로 Linux와 Windows에서 작동 방식에 큰 차이는 없습니다.
1. Linux에서 Linux 컨테이너 실행
• 원리: 컨테이너화의 근간은 Linux Container (LXC) 형식에 있습니다. LXC는 단일 Linux 커널을 사용하여 여러 격리된 Linux 시스템(컨테이너)을 제어 호스트에서 실행하는 운영 체제 수준의 가상화 방법입니다. 컨테이너는 자체 OS가 필요 없으므로 VM보다 훨씬 가볍고, 서버나 호스트의 모든 컨테이너가 단일 OS 커널을 공유하여 저장 공간, CPU, RAM과 같은 막대한 컴퓨팅 리소스를 절약합니다. Docker는 기본적으로 Linux 기능인 네임스페이스, 제어 그룹, 유니온 파일 시스템 등을 활용합니다.
• 실행 환경: Docker는 Linux 커널 3.10 이상을 사용하는 모든 Linux 시스템에서 실행됩니다. 최신 버전의 Linux 커널이 cgroup 및 네임스페이스 격리 기능을 기본적으로 지원하기 때문에 Linux 호스트에서는 Docker Engine을 직접 실행할 수 있습니다. 이는 Docker가 Linux 시스템에서 "네이티브하게" 작동한다는 것을 의미합니다.
• 이점: 하나의 Linux 배포판에서 실행되는 컨테이너는 최소한의 노력으로 다른 Linux 배포판으로 이동할 수 있어 개발자에게 매우 편리합니다.



## 2. Windows 및 Mac에서 Linux 컨테이너 실행
• 원리: Linux만이 컨테이너 실행에 필요한 핵심 기능을 노출하기 때문에,
	Windows 및 macOS 호스트는 백그라운드에서 **Linux 가상 머신(VM)**을 활용하여 컨테이너 실행을 가능하게 합니다. 
	Docker Desktop은 Windows 및 macOS 사용자를 위해 이 VM을 백그라운드에서 배포하고 실행합니다. 
	이 덕분에 사용자는 마치 Docker 명령이 macOS 또는 Windows 호스트의 터미널이나 PowerShell 콘솔에서 기본적으로 실행되는 것처럼 느낄 수 있습니다.

• 실행 환경: Docker Desktop은 기본 가상 머신을 사용자에게 숨겨주며, macOS에서는 이 경험이 거의 원활하다고 언급됩니다. 그러나 Windows에서는 기업 방화벽, 공격적인 안티바이러스 구성, 셸 기본 설정, 그리고 여러 간접 계층으로 인해 더 많은 구성상의 변형을 다루어야 할 수 있어 작성된 콘텐츠가 빠르게 구식이 될 수 있습니다.

• 제한 사항: Windows 및 macOS의 운영 체제 아키텍처(네트워킹 및 프로세스 관리 측면)가 Linux와 근본적으로 다르기 때문에, 특정 네트워킹 구성(예: MACVLAN 드라이버)은 Docker Desktop for Mac, Docker Desktop for Windows 또는 Docker EE for Windows Server에서 지원되지 않으며 Linux 호스트에서만 작동합니다. 또한, Docker는 명령줄 인터페이스가 있는 애플리케이션 컨테이너화를 위해 설계되었기 때문에, Windows 및 Linux 모두에서 애플리케이션 내부의 그래픽 인터페이스에 연결하는 네이티브 방식이 부족합니다. 이는 Linux보다 GUI 사용이 더 일반적인 Windows에서 병목 현상으로 작용할 수 있습니다.


## Windows에서 Linux 컨테이너를 실행하기 위해 WSL2가 필요한 이유

Linux 컨테이너는 Linux 커널의 특정 기능인 네임스페이스(namespaces) 및 **제어 그룹(cgroups)**을 사용하여 프로세스 수준의 격리를 제공합니다. 이러한 기능은 컨테이너가 자체 운영 체제 없이도 격리된 환경에서 실행될 수 있도록 하는 핵심 기술입니다.
Windows 운영 체제는 이러한 Linux 커널의 고유한 기능을 직접 제공하지 않습니다. 따라서 Windows에서 Linux 컨테이너를 실행하려면, 컨테이너가 의존하는 Linux 커널 환경이 필요합니다. 전통적으로 Docker Desktop은 이 Linux 커널 환경을 제공하기 위해 백그라운드에서 경량의 가상 머신을 실행했습니다.
**WSL2(Windows Subsystem for Linux 2)**는 이러한 필요성을 해결하기 위해 도입된 기술입니다. WSL2는 Windows에 경량 Linux 커널을 통합하는 가상화 기술을 사용하여, Windows 환경 내에서 완전한 Linux 시스템을 실행할 수 있도록 합니다.
따라서 Windows에서 Linux 컨테이너를 실행하기 위해 WSL2가 필요한 이유는 다음과 같습니다:
1. Linux 커널 종속성: Linux 컨테이너는 Linux 커널의 특정 격리 기능(네임스페이스, cgroups)에 의존하여 작동합니다. Windows는 이 기능을 기본적으로 제공하지 않습니다.
2. VM 효율성 및 통합: WSL2는 기존의 무거운 가상 머신 솔루션보다 훨씬 효율적이고 Windows 시스템에 더 깊이 통합된 방식으로 Linux 커널을 제공합니다. 이는 컨테이너의 시작 시간을 단축하고 전반적인 성능을 향상시키는 데 기여합니다.
3. Docker Desktop과의 연동: Docker for Windows를 사용할 때, WSL2는 Linux 컨테이너를 실행하는 데 필요한 백그라운드 Linux 환경을 제공하는 메커니즘으로 활용될 수 있습니다. 이는 Windows 사용자가 Linux 환경에 직접 접근할 필요 없이 Linux 컨테이너를 원활하게 실행할 수 있도록 돕습니다.
요약하자면, WSL2는 Windows 시스템에서 Linux 컨테이너가 요구하는 필수 Linux 커널 기능을 효율적으로 제공함으로써, Windows 사용자가 마치 네이티브 Linux 환경처럼 컨테이너를 실행하고 관리할 수 있도록 해주는 핵심 구성 요소입니다.

