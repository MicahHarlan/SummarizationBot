import torch
from transformers import AutoTokenizer, AutoModelWithLMHead

tokenizer=AutoTokenizer.from_pretrained('T5-base')
model=AutoModelWithLMHead.from_pretrained('T5-base', return_dict=True)

sequence = ("We close with a brief discussion of K-nearest neighbors (KNN), intro- duced in Chapter 2. Recall that KNN takes a completely different approach from the classifiers seen in this chapter. In order to make a prediction for an observation X = x, the training observations that are closest to x are identified. Then X is assigned to the class to which the plurality of these observations belong. Hence KNN is a completely non-parametric approach: no assumptions are made about the shape of the decision boundary. We make the following observations about KNN:Because KNN is completely non-parametric, we can expect this ap- proach to dominate LDA and logistic regression when the decision boundary is highly non-linear, provided that n is very large and p is small.In order to provide accurate classification, KNN requires a lot of ob- servations relative to the number of predictors—that is, n much larger than p. This has to do with the fact that KNN is non-parametric, and thus tends to reduce the bias while incurring a lot of variance. In settings where the decision boundary is non-linear but n is only modest, or p is not very small, then QDA may be preferred to KNN. This is because QDA can provide a non-linear decision boundary while taking advantage of a parametric form, which means that it requires a smaller sample size for accurate classification, relative to KNN. Unlike logistic regression, KNN does not tell us which predictors are important: we don’t get a table of coefficients as in Table 4.3.")

inputs=tokenizer.encode("sumarize: " +sequence,return_tensors='pt', max_length=512, truncation=True)
output = model.generate(inputs, min_length=80, max_length=100)

summary=tokenizer.decode(output[0])
print(summary)

