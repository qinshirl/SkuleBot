# SkuleBot

## pdf to markdowm
use dolphin to convert
https://github.com/bytedance/Dolphin

Feng, H., Wei, S., Fei, X., Shi, W., Han, Y., Liao, L., … & others. (2025). *Dolphin: Document Image Parsing via Heterogeneous Anchor Prompting*. arXiv preprint [arXiv:2505.14059](https://arxiv.org/abs/2505.14059).

### instructions
```text
git clone https://github.com/ByteDance/Dolphin.git
cd Dolphin
pip install -r requirements.txt   (use python 3.11)
pip install huggingface_hub
huggingface-cli download ByteDance/Dolphin-1.5 --local-dir ./hf_model
python demo_page.py --model_path ./hf_model --save_dir ./results \
    --input_path (our pdf file)
```