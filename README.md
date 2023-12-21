# Download models
Run the following command to download the models:
```bash
python download_model.py
```

# Install requirements
Run the following command to install the requirements:
```bash
./prepare.sh
```

# Inference
Navigate to the `vits` directory:
```bash
cd vits
```

## Russian
To run inference for Russian language, use the following command:
```bash
CUDA_VISIBLE_DEVICES=2 python inference.py --lang rus --transcript_file ../transcripts_ru.txt --output_dir ../out_ru
```

# Support languages
- [ ]  Japanese
- [ ]  Chinese
- [x]  Russian
- [x]  Korean
- [x]  French
- [x]  German
- [x]  Vietnamese
- [x]  Thai
- [x]  Hindi
- [x]  Arabic