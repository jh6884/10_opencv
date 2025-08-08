#!/usr/bin/env python3
"""
단순화된 YouTube 영상 다운로드 스크립트
yt-dlp와 ffmpeg를 사용하여 YouTube 영상을 다운로드합니다.
"""

import os
import subprocess
from pathlib import Path

def download_video(url, output_dir="downloads", quality="best", format_type="mp4"):
    """
    YouTube 영상 다운로드
    
    Args:
        url (str): YouTube 영상 URL
        output_dir (str): 다운로드 폴더
        quality (str): 화질 설정 (best, worst, 720p, 1080p 등)
        format_type (str): 출력 포맷 (mp4, mkv, webm 등)
    """
    
    # 출력 디렉토리 생성
    Path(output_dir).mkdir(exist_ok=True)
    
    # 출력 파일명 템플릿
    output_template = os.path.join(output_dir, '%(title)s.%(ext)s')
    
    # yt-dlp 명령어 구성
    cmd = [
        'yt-dlp',
        '--format', f'{quality}[ext={format_type}]/best[ext={format_type}]/best',
        '--output', output_template,
        '--embed-subs',  # 자막 포함
        '--write-sub',   # 자막 파일 별도 저장
        '--sub-langs', 'ko,en',  # 한국어, 영어 자막
        url
    ]
    
    try:
        print(f"다운로드 시작: {url}")
        print(f"저장 위치: {output_dir}")
        print(f"품질: {quality}, 포맷: {format_type}")
        print("-" * 50)
        
        # 다운로드 실행
        result = subprocess.run(cmd, check=True)
        print("다운로드 완료!")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"다운로드 실패: {e}")
        return False

def get_video_info(url):
    """영상 정보 가져오기"""
    cmd = [
        'yt-dlp',
        '--print', '%(title)s',
        '--print', '%(duration)s',
        '--print', '%(uploader)s',
        '--print', '%(view_count)s',
        '--no-download',
        url
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        lines = result.stdout.strip().split('\n')
        
        if len(lines) >= 4:
            return {
                'title': lines[0],
                'duration': f"{int(lines[1])//60}:{int(lines[1])%60:02d}" if lines[1].isdigit() else lines[1],
                'uploader': lines[2],
                'views': lines[3]
            }
    except subprocess.CalledProcessError:
        return None
    
    return None

def main():
    """메인 함수"""
    print("=== YouTube 영상 다운로더 ===")
    print()
    
    # URL 입력
    url = input("YouTube URL을 입력하세요: ").strip()
    if not url:
        print("URL이 입력되지 않았습니다.")
        return
    
    # 영상 정보 표시
    print("\n영상 정보를 가져오는 중...")
    info = get_video_info(url)
    if info:
        print(f"제목: {info['title']}")
        print(f"재생시간: {info['duration']}")
        print(f"업로더: {info['uploader']}")
        print(f"조회수: {info['views']}")
        print()
    
    # 다운로드 옵션 선택
    print("다운로드 옵션을 선택하세요:")
    print("1. 영상 다운로드 (기본 품질)")
    print("2. 영상 다운로드 (고화질 1080p)")
    print("3. 영상 다운로드 (저화질 720p)")
    print("4. 사용자 정의 설정")
    
    choice = input("선택 (1-4): ").strip()
    
    output_dir = input("다운로드 폴더 (기본: downloads): ").strip() or "downloads"
    
    if choice == "1":
        download_video(url, output_dir)
    elif choice == "2":
        download_video(url, output_dir, quality="1080p")
    elif choice == "3":
        download_video(url, output_dir, quality="720p")
    elif choice == "4":
        quality = input("품질 (best/worst/720p/1080p): ").strip() or "best"
        format_type = input("포맷 (mp4/mkv/webm): ").strip() or "mp4"
        download_video(url, output_dir, quality, format_type)
    else:
        print("잘못된 선택입니다.")

if __name__ == "__main__":
    main()