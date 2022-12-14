# SpeedRead

![SpeedRead Logo](https://github.com/AterhiM/TextPointer/blob/main/app/pictures/speedread_logo.jpg)

## What is it?

This is a Streamlit application for text highlighting, that aims to help reading text faster.

The solution is introduced as a highlighting of a part of the words in text which is the only thing in a word that the human brain would need to understand the entire meaning of the sentence.


## How to run?

**1. Clone the repository:**

```bash
git clone "https://github.com/AterhiM/SpeedRead.git"
```

**2. Build docker image:**

```bash
docker build -t speed-read-demo-image .
```

**3. Run the application using docker-compose:**

```bash
docker-compose -f ./docker-compose.yml up
```

## Contributing

For major changes, please open an issue first to discuss what you would like to change. 
Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
