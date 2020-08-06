'TypeError: '_io.TextIOWrapper' 와 제한시간 초과의 벽을 넘지 못하고 여기서 잠들다...





++

200806

 결국 제출되어 있는 답들을 살펴 보고 뒤에서부터 접근하면 시간 접근을 줄일 수 있다는 것을 배웠다. 그렇지만 '_io.TextIOWrapper'는 해결하지 못했음

++

200806

파일 여는 코드를 잘못 넣은 거였음...

```
import sys
sys.stdin = open('input.txt', 'r')
```

머 했냐 ...