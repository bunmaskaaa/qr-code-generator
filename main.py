import argparse, os, time, logging
import qrcode

os.makedirs("qr_codes", exist_ok=True)
os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)

def generate_qr(url: str) -> str:
    img = qrcode.make(url)
    path = f"qr_codes/qr_{int(time.time())}.png"
    img.save(path)
    return path

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="QR Code Generator")
    parser.add_argument("--url", default="http://github.com/kaw393939")
    args = parser.parse_args()
    result = generate_qr(args.url)
    logging.info(f"Generated QR for {args.url} -> {result}")
    print(f"Saved: {result}")