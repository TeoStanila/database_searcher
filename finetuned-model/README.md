---
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- dense
- generated_from_trainer
- dataset_size:11943
- loss:MultipleNegativesRankingLoss
base_model: sentence-transformers/all-MiniLM-L6-v2
widget:
- source_sentence: vendors outside sweden
  sentences:
  - 'ECrowd Invest Located in Barcelona, Catalonia, spain. Founded in 2014. Business
    model: business-to-consumer. Target markets: sustainable finance, environmental
    services. Offerings include Crowd Lending Platform Services, Sustainable Investment
    Opportunity Facilitation, Environmental Project Investment Facilitation, Social
    Project Investment Facilitation. ecrowd invest is a spanish private entity operating
    as an online crowd lending platform specialized in facilitating investment opportunities
    in environmental and social projects.'
  - 'Domaine Godeau Located in beaulieu-sur-layon, pays de la loire, france. Business
    model: manufacturing. Target markets: food and beverage. Offerings include Wine
    Production, Beverage Manufacturing, Food Product Manufacturing. domaine godeau
    is a french beverage manufacturer and wine producer operating in the food production
    sector. the company is based in beaulieu-sur-layon, pays de la loire, france,
    and specializes in the manufacturing of beverages and food products.'
  - 'Paniers d''Eve Located in canet, occitania, france. Business model: manufacturing.
    Target markets: food and beverage. Offerings include Food Manufacturing, Crop
    Growing Production, Truck Farming Production, Fruit and Vegetable Processing.
    paniers d''eve is a french food manufacturer operating in crop growing, fruit
    and vegetable processing, and truck farming.'
- source_sentence: manufacturers excluding egypt
  sentences:
  - 'Rögle Vindkraftpark Located in Ängelholm, Skåne County, sweden. Business model:
    retail, manufacturing, business-to-consumer. Target markets: renewable energy.
    Offerings include Solar Energy Equipment Supply, Wind Turbine Construction. rögle
    vindkraftpark is a swedish company operating in the solar energy sector, functioning
    as both a supplier of solar energy equipment and a builder of wind turbines.'
  - 'ECrowd Invest Located in Barcelona, Catalonia, spain. Founded in 2014. Business
    model: business-to-consumer. Target markets: sustainable finance, environmental
    services. Offerings include Crowd Lending Platform Services, Sustainable Investment
    Opportunity Facilitation, Environmental Project Investment Facilitation, Social
    Project Investment Facilitation. ecrowd invest is a spanish private entity operating
    as an online crowd lending platform specialized in facilitating investment opportunities
    in environmental and social projects.'
  - 'ECrowd Invest Located in Barcelona, Catalonia, spain. Founded in 2014. Business
    model: business-to-consumer. Target markets: sustainable finance, environmental
    services. Offerings include Crowd Lending Platform Services, Sustainable Investment
    Opportunity Facilitation, Environmental Project Investment Facilitation, Social
    Project Investment Facilitation. ecrowd invest is a spanish private entity operating
    as an online crowd lending platform specialized in facilitating investment opportunities
    in environmental and social projects.'
- source_sentence: manufacturers excluding egypt
  sentences:
  - 'MILHADE Vins & Spiritueux Located in libourne, nouvelle-aquitaine, france. Founded
    in 1938. Business model: manufacturing. Target markets: food and beverage. Offerings
    include Wine Production, Sustainable Beverage Production Practices, Spirit Beverage
    Production, Beverage Manufacturing, Community-Focused Beverage Distribution, Collaborative
    Winemaking Partnership Development. milhade vins & spiritueux is a french beverage
    manufacturer operating in the food production sector. the company serves vignerons,
    distributors, and clients in the nouvelle-aquitaine region.'
  - 'MILHADE Vins & Spiritueux Located in libourne, nouvelle-aquitaine, france. Founded
    in 1938. Business model: manufacturing. Target markets: food and beverage. Offerings
    include Wine Production, Sustainable Beverage Production Practices, Spirit Beverage
    Production, Beverage Manufacturing, Community-Focused Beverage Distribution, Collaborative
    Winemaking Partnership Development. milhade vins & spiritueux is a french beverage
    manufacturer operating in the food production sector. the company serves vignerons,
    distributors, and clients in the nouvelle-aquitaine region.'
  - 'Rögle Vindkraftpark Located in Ängelholm, Skåne County, sweden. Business model:
    retail, manufacturing, business-to-consumer. Target markets: renewable energy.
    Offerings include Solar Energy Equipment Supply, Wind Turbine Construction. rögle
    vindkraftpark is a swedish company operating in the solar energy sector, functioning
    as both a supplier of solar energy equipment and a builder of wind turbines.'
- source_sentence: vendors outside sweden
  sentences:
  - 'Famille Pouille Located in bonneville, auvergne-rhône-alpes, france. Reports
    revenue of about 200000. Business model: manufacturing. Target markets: food and
    beverage. Offerings include Food and Beverage Production, Food and Beverage Manufacturing.
    famille pouille is a french company specialized in the manufacturing and production
    of food and beverage products. the company operates primarily in the food and
    beverage sector.'
  - 'Carita och Torbjörn Located in Lekebergs kommun, Örebro County, sweden. Business
    model: retail, business-to-business, manufacturing, business-to-consumer. Target
    markets: renewable energy. Offerings include Renewable Energy Solutions, Wind
    Power Equipment Services, Wind Power Park Operation, Wind Power Equipment Manufacturing,
    Wind Power Equipment Retail. carita och torbjörn is a swedish company specialized
    in the production and sale of wind power equipment and related services. the company
    operates a wind power park in kronoberget, serving customers interested in renewable
    energy solutions.'
  - 'Rhino Power Located in Läyliäinen, Kanta-Häme, finland. Founded in 2009. Reports
    revenue of about 16095954. Business model: business-to-business, manufacturing,
    wholesale. Target markets: renewable energy. Offerings include Power Generation
    Equipment Distribution, Renewable Energy Equipment Manufacturing, Renewable Energy
    Equipment Distribution, Power Generation Equipment Manufacturing. rhino power
    oy is a finnish company engaged in the production and distribution of power generation
    equipment, with a focus on renewable energy solutions. the company primarily serves
    clients in the energy industry.'
- source_sentence: vendors outside sweden
  sentences:
  - 'Erikshester Vindpark Located in Vetlanda kommun, Jönköping County, sweden. Reports
    revenue of about 101017584. Business model: business-to-business, manufacturing,
    wholesale. Target markets: renewable energy. Offerings include Wind Turbine Operation,
    Wind Turbine Manufacturing, Wind Turbine Supply, Renewable Energy Solutions. erikshester
    vindpark ab, dba erikshester vindpark, is a swedish company specialized in the
    production and operation of wind turbines and renewable energy solutions. the
    company primarily serves industrial clients and the renewable energy sector in
    local and regional markets.'
  - 'Domaine Godeau Located in beaulieu-sur-layon, pays de la loire, france. Business
    model: manufacturing. Target markets: food and beverage. Offerings include Wine
    Production, Beverage Manufacturing, Food Product Manufacturing. domaine godeau
    is a french beverage manufacturer and wine producer operating in the food production
    sector. the company is based in beaulieu-sur-layon, pays de la loire, france,
    and specializes in the manufacturing of beverages and food products.'
  - 'Erikshester Vindpark Located in Vetlanda kommun, Jönköping County, sweden. Reports
    revenue of about 101017584. Business model: business-to-business, manufacturing,
    wholesale. Target markets: renewable energy. Offerings include Wind Turbine Operation,
    Wind Turbine Manufacturing, Wind Turbine Supply, Renewable Energy Solutions. erikshester
    vindpark ab, dba erikshester vindpark, is a swedish company specialized in the
    production and operation of wind turbines and renewable energy solutions. the
    company primarily serves industrial clients and the renewable energy sector in
    local and regional markets.'
pipeline_tag: sentence-similarity
library_name: sentence-transformers
metrics:
- cosine_accuracy@10
- cosine_precision@10
- cosine_recall@10
- cosine_ndcg@10
- cosine_mrr@10
- cosine_map@100
model-index:
- name: SentenceTransformer based on sentence-transformers/all-MiniLM-L6-v2
  results:
  - task:
      type: information-retrieval
      name: Information Retrieval
    dataset:
      name: test
      type: test
    metrics:
    - type: cosine_accuracy@10
      value: 0.8333333333333334
      name: Cosine Accuracy@10
    - type: cosine_precision@10
      value: 0.36
      name: Cosine Precision@10
    - type: cosine_recall@10
      value: 0.5006809357270726
      name: Cosine Recall@10
    - type: cosine_ndcg@10
      value: 0.5968453179926297
      name: Cosine Ndcg@10
    - type: cosine_mrr@10
      value: 0.5797619047619047
      name: Cosine Mrr@10
    - type: cosine_map@100
      value: 0.5994769472632121
      name: Cosine Map@100
---

# SentenceTransformer based on sentence-transformers/all-MiniLM-L6-v2

This is a [sentence-transformers](https://www.SBERT.net) model finetuned from [sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2). It maps inputs to a 384-dimensional dense vector space and can be used for semantic textual similarity, semantic search, paraphrase mining, classification, clustering, and more.

## Model Details

### Model Description
- **Model Type:** Sentence Transformer
- **Base model:** [sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) <!-- at revision 1110a243fdf4706b3f48f1d95db1a4f5529b4d41 -->
- **Maximum Sequence Length:** 256 tokens
- **Output Dimensionality:** 384 dimensions
- **Similarity Function:** Cosine Similarity
- **Supported Modality:** Text
<!-- - **Training Dataset:** Unknown -->
<!-- - **Language:** Unknown -->
<!-- - **License:** Unknown -->

### Model Sources

- **Documentation:** [Sentence Transformers Documentation](https://sbert.net)
- **Repository:** [Sentence Transformers on GitHub](https://github.com/huggingface/sentence-transformers)
- **Hugging Face:** [Sentence Transformers on Hugging Face](https://huggingface.co/models?library=sentence-transformers)

### Full Model Architecture

```
SentenceTransformer(
  (0): Transformer({'transformer_task': 'feature-extraction', 'modality_config': {'text': {'method': 'forward', 'method_output_name': 'last_hidden_state'}}, 'module_output_name': 'token_embeddings', 'architecture': 'BertModel'})
  (1): Pooling({'embedding_dimension': 384, 'pooling_mode': 'mean', 'include_prompt': True})
  (2): Normalize({'module_input_name': 'sentence_embedding', 'module_output_name': 'sentence_embedding'})
)
```

## Usage

### Direct Usage (Sentence Transformers)

First install the Sentence Transformers library:

```bash
pip install -U sentence-transformers
```
Then you can load this model and run inference.
```python
from sentence_transformers import SentenceTransformer

# Download from the 🤗 Hub
model = SentenceTransformer("sentence_transformers_model_id")
# Run inference
queries = [
    'vendors outside sweden',
]
documents = [
    'Domaine Godeau Located in beaulieu-sur-layon, pays de la loire, france. Business model: manufacturing. Target markets: food and beverage. Offerings include Wine Production, Beverage Manufacturing, Food Product Manufacturing. domaine godeau is a french beverage manufacturer and wine producer operating in the food production sector. the company is based in beaulieu-sur-layon, pays de la loire, france, and specializes in the manufacturing of beverages and food products.',
    'Erikshester Vindpark Located in Vetlanda kommun, Jönköping County, sweden. Reports revenue of about 101017584. Business model: business-to-business, manufacturing, wholesale. Target markets: renewable energy. Offerings include Wind Turbine Operation, Wind Turbine Manufacturing, Wind Turbine Supply, Renewable Energy Solutions. erikshester vindpark ab, dba erikshester vindpark, is a swedish company specialized in the production and operation of wind turbines and renewable energy solutions. the company primarily serves industrial clients and the renewable energy sector in local and regional markets.',
    'Erikshester Vindpark Located in Vetlanda kommun, Jönköping County, sweden. Reports revenue of about 101017584. Business model: business-to-business, manufacturing, wholesale. Target markets: renewable energy. Offerings include Wind Turbine Operation, Wind Turbine Manufacturing, Wind Turbine Supply, Renewable Energy Solutions. erikshester vindpark ab, dba erikshester vindpark, is a swedish company specialized in the production and operation of wind turbines and renewable energy solutions. the company primarily serves industrial clients and the renewable energy sector in local and regional markets.',
]
query_embeddings = model.encode_query(queries)
document_embeddings = model.encode_document(documents)
print(query_embeddings.shape, document_embeddings.shape)
# [1, 384] [3, 384]

# Get the similarity scores for the embeddings
similarities = model.similarity(query_embeddings, document_embeddings)
print(similarities)
# tensor([[0.3052, 0.5074, 0.5074]])
```
<!--
### Direct Usage (Transformers)

<details><summary>Click to see the direct usage in Transformers</summary>

</details>
-->

<!--
### Downstream Usage (Sentence Transformers)

You can finetune this model on your own dataset.

<details><summary>Click to expand</summary>

</details>
-->

<!--
### Out-of-Scope Use

*List how the model may foreseeably be misused and address what users ought not to do with the model.*
-->

## Evaluation

### Metrics

#### Information Retrieval

* Dataset: `test`
* Evaluated with [<code>InformationRetrievalEvaluator</code>](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#sentence_transformers.sentence_transformer.evaluation.InformationRetrievalEvaluator)

| Metric              | Value      |
|:--------------------|:-----------|
| cosine_accuracy@10  | 0.8333     |
| cosine_precision@10 | 0.36       |
| cosine_recall@10    | 0.5007     |
| **cosine_ndcg@10**  | **0.5968** |
| cosine_mrr@10       | 0.5798     |
| cosine_map@100      | 0.5995     |

<!--
## Bias, Risks and Limitations

*What are the known or foreseeable issues stemming from this model? You could also flag here known failure cases or weaknesses of the model.*
-->

<!--
### Recommendations

*What are recommendations with respect to the foreseeable issues? For example, filtering explicit content.*
-->

## Training Details

### Training Dataset

#### Unnamed Dataset

* Size: 11,943 training samples
* Columns: <code>anchor</code> and <code>positive</code>
* Approximate statistics based on the first 100 samples:
  |          | anchor                                                                         | positive                                                                             |
  |:---------|:-------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------|
  | type     | string                                                                         | string                                                                               |
  | modality | text                                                                           | text                                                                                 |
  | details  | <ul><li>min: 4 tokens</li><li>mean: 4.0 tokens</li><li>max: 4 tokens</li></ul> | <ul><li>min: 95 tokens</li><li>mean: 203.81 tokens</li><li>max: 256 tokens</li></ul> |
* Samples:
  | anchor                             | positive                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
  |:-----------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | <code>enterprise businesses</code> | <code>Rompetrol Located in bucharest, romania. Founded in 1979. Reports revenue of about 13498241905. Business model: wholesale, manufacturing, business-to-business, retail, service provider, business-to-consumer, enterprise. Target markets: energy, industrial, transportation. Offerings include Fuel Product Distribution, Quality and Safety Compliance Services, Petrochemical Product Manufacturing, E-Mobility Solutions Implementation, Petroleum Refining and Distribution, Premium Fuel Retail. rompetrol is a romanian company specialized in petroleum refining, petrochemical operations, and the distribution of fuel products. the company operates as a subsidiary of kmg international and manages integrated refineries in romania, moldova, bulgaria, and georgia, serving the automotive, industrial, and energy sectors. rompetrol also provides industrial products, wholesale fuel supply, and e-mobility services, and is certified for quality, health, safety, and environmental management.</code>                       |
  | <code>enterprise businesses</code> | <code>Rompetrol Located in bucharest, romania. Founded in 1974. Has about 7000 employees. Reports revenue of about 12664964365. Business model: wholesale, manufacturing, business-to-business, retail, service provider, business-to-consumer, enterprise. Target markets: energy, petrochemicals. Offerings include Sustainable Energy Solutions, Fuel and Energy Product Retail, Energy Project Development, Petrochemical Product Manufacturing, Consumer Energy Product Retail, Decarbonization and Green Energy Solutions. rompetrol is a romanian energy company engaged in refining, petrochemicals, and retail operations, as well as providing well services in the upstream sector. the company supplies fuels and related products to both individual and business clients in romania, moldova, bulgaria, georgia, and kazakhstan, and is involved in the development of energy projects through its participation in the kazakh-romanian energy investment fund. rompetrol also manages a supply chain and logistics network to s...</code> |
  | <code>enterprise businesses</code> | <code>CBRE Romania Located in bucharest, romania. Founded in 2008. Has about 92 employees. Reports revenue of about 9568739216. Business model: service provider, business-to-business, enterprise. Target markets: hospitality, retail, industrial, real estate, logistics. Offerings include Data Center Real Estate Services, Real Estate Research and Analysis Services, Mortgage and Capital Markets Services, Portfolio Management Services, Property Investment and Finance Services, Project Management Services. cbre romania is a romanian company engaged in commercial real estate services and investment, providing integrated solutions such as investment, finance, value creation, planning, leasing, occupancy, design, building, property management, and portfolio management. the company serves clients in sectors including hotels, office, retail, industrial, logistics, and alternative property types, as well as data center services. cbre romania also offers transaction management, project management, design...</code> |
* Loss: [<code>MultipleNegativesRankingLoss</code>](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#multiplenegativesrankingloss) with these parameters:
  ```json
  {
      "scale": 20.0,
      "similarity_fct": "cos_sim",
      "gather_across_devices": false,
      "directions": [
          "query_to_doc"
      ],
      "partition_mode": "joint",
      "hardness_mode": null,
      "hardness_strength": 0.0
  }
  ```

### Evaluation Dataset

#### Unnamed Dataset

* Size: 1,789 evaluation samples
* Columns: <code>anchor</code> and <code>positive</code>
* Approximate statistics based on the first 100 samples:
  |          | anchor                                                                          | positive                                                                             |
  |:---------|:--------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------|
  | type     | string                                                                          | string                                                                               |
  | modality | text                                                                            | text                                                                                 |
  | details  | <ul><li>min: 5 tokens</li><li>mean: 5.19 tokens</li><li>max: 9 tokens</li></ul> | <ul><li>min: 94 tokens</li><li>mean: 196.43 tokens</li><li>max: 256 tokens</li></ul> |
* Samples:
  | anchor                                     | positive                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
  |:-------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | <code>manufacturers human resources</code> | <code>Bizneo HR Located in Madrid, Community of Madrid, spain. Founded in 2013. Has about 174 employees. Reports revenue of about 24680239. Business model: business-to-business, enterprise, software-as-a-service. Target markets: human resources. Offerings include Time Management Software Development, HR Software Scalability Solutions, HR Software Customization Services, Performance Management Software Development, Recruitment Source Management Software Development, Cloud-Based HR Management Software Development. bizneo solutions s.l., dba bizneo hr, is a spanish company specialized in human resources software solutions, including cloud-based hr management platforms and recruitment technology. the company develops and provides a suite of hr software modules, such as talent management, core hr, time management, recruiting, performance management, training management, and employee surveys, serving clients in spain and internationally across more than 40 countries. bizneo hr also offers a mobile...</code> |
  | <code>manufacturers human resources</code> | <code>Sincron HR Located in Bucharest, romania. Founded in 2007. Has about 15 employees. Reports revenue of about 1014952. Business model: service provider, business-to-business, enterprise, software-as-a-service. Target markets: human resources. Offerings include HR Software User Training Services, HR Software Customization Services, HR Management Platform Solutions, Performance Management Software Development, Training Management Software Development, Talent Management Software Development. hr sincron srl, dba sincron hr, is a romanian software company specialized in providing hr software solutions, including recruitment, talent management, and hr analytics. the company offers a comprehensive platform that covers areas such as recruitment, onboarding, staffing, time and attendance, payroll, performance management, training management, employee self-service, internal communication, and hr analytics. sincron hr serves clients across europe and north america, supporting businesses of various ...</code> |
  | <code>manufacturers human resources</code> | <code>BCS HR Software Located in 's-Hertogenbosch, North Brabant, netherlands. Founded in 1978. Has about 5 employees. Reports revenue of about 1313795. Business model: service provider, business-to-business, enterprise, software-as-a-service. Target markets: human resources. Offerings include HR Onboarding and Offboarding Solutions Development, Learning and Development Management Solutions Development, Payroll Administration Software Development, HR Software Implementation and Consulting Services, HR Outsourcing Services, Leave and Absenteeism Tracking Software Development. bcs b.v., dba bcs hr software, is a dutch company that develops and provides hr management and payroll administration software. the company offers a modular suite of hrm and payroll solutions, including modules for recruitment, leave management, expense management, hr analytics, workflows, onboarding, offboarding, time tracking, and benefits administration. bcs hr software also provides payroll outsourcing, hr analytics,...</code> |
* Loss: [<code>MultipleNegativesRankingLoss</code>](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#multiplenegativesrankingloss) with these parameters:
  ```json
  {
      "scale": 20.0,
      "similarity_fct": "cos_sim",
      "gather_across_devices": false,
      "directions": [
          "query_to_doc"
      ],
      "partition_mode": "joint",
      "hardness_mode": null,
      "hardness_strength": 0.0
  }
  ```

### Training Hyperparameters
#### Non-Default Hyperparameters

- `per_device_train_batch_size`: 128
- `num_train_epochs`: 10
- `learning_rate`: 2e-05
- `fp16`: True
- `per_device_eval_batch_size`: 128
- `batch_sampler`: no_duplicates

#### All Hyperparameters
<details><summary>Click to expand</summary>

- `per_device_train_batch_size`: 128
- `num_train_epochs`: 10
- `max_steps`: -1
- `learning_rate`: 2e-05
- `lr_scheduler_type`: linear
- `lr_scheduler_kwargs`: None
- `warmup_steps`: 0
- `optim`: adamw_torch_fused
- `optim_args`: None
- `weight_decay`: 0.0
- `adam_beta1`: 0.9
- `adam_beta2`: 0.999
- `adam_epsilon`: 1e-08
- `optim_target_modules`: None
- `gradient_accumulation_steps`: 1
- `average_tokens_across_devices`: True
- `max_grad_norm`: 1.0
- `label_smoothing_factor`: 0.0
- `bf16`: False
- `fp16`: True
- `bf16_full_eval`: False
- `fp16_full_eval`: False
- `tf32`: None
- `gradient_checkpointing`: False
- `gradient_checkpointing_kwargs`: None
- `torch_compile`: False
- `torch_compile_backend`: None
- `torch_compile_mode`: None
- `use_liger_kernel`: False
- `liger_kernel_config`: None
- `use_cache`: False
- `neftune_noise_alpha`: None
- `torch_empty_cache_steps`: None
- `auto_find_batch_size`: False
- `log_on_each_node`: True
- `logging_nan_inf_filter`: True
- `include_num_input_tokens_seen`: no
- `log_level`: passive
- `log_level_replica`: warning
- `disable_tqdm`: False
- `project`: huggingface
- `trackio_space_id`: None
- `trackio_bucket_id`: None
- `trackio_static_space_id`: None
- `per_device_eval_batch_size`: 128
- `prediction_loss_only`: True
- `eval_on_start`: False
- `eval_do_concat_batches`: True
- `eval_use_gather_object`: False
- `eval_accumulation_steps`: None
- `include_for_metrics`: []
- `batch_eval_metrics`: False
- `save_only_model`: False
- `save_on_each_node`: False
- `enable_jit_checkpoint`: False
- `push_to_hub`: False
- `hub_private_repo`: None
- `hub_model_id`: None
- `hub_strategy`: every_save
- `hub_always_push`: False
- `hub_revision`: None
- `load_best_model_at_end`: False
- `ignore_data_skip`: False
- `restore_callback_states_from_checkpoint`: False
- `full_determinism`: False
- `seed`: 42
- `data_seed`: None
- `use_cpu`: False
- `accelerator_config`: {'split_batches': False, 'dispatch_batches': None, 'even_batches': True, 'use_seedable_sampler': True, 'non_blocking': False, 'gradient_accumulation_kwargs': None}
- `parallelism_config`: None
- `dataloader_drop_last`: False
- `dataloader_num_workers`: 0
- `dataloader_pin_memory`: True
- `dataloader_persistent_workers`: False
- `dataloader_prefetch_factor`: None
- `dataloader_multiprocessing_context`: None
- `dataloader_in_order`: True
- `remove_unused_columns`: True
- `label_names`: None
- `train_sampling_strategy`: random
- `length_column_name`: length
- `ddp_find_unused_parameters`: None
- `ddp_bucket_cap_mb`: None
- `ddp_broadcast_buffers`: False
- `ddp_static_graph`: None
- `ddp_backend`: None
- `ddp_timeout`: 1800
- `fsdp`: None
- `fsdp_config`: None
- `deepspeed`: None
- `debug`: []
- `skip_memory_metrics`: True
- `do_predict`: False
- `resume_from_checkpoint`: None
- `local_rank`: -1
- `prompts`: None
- `batch_sampler`: no_duplicates
- `multi_dataset_batch_sampler`: proportional
- `router_mapping`: {}
- `learning_rate_mapping`: {}
- `warmup_ratio`: None

</details>

### Training Logs
| Epoch | Step | Training Loss | test_cosine_ndcg@10 |
|:-----:|:----:|:-------------:|:-------------------:|
| 1.0   | 94   | 3.7641        | -                   |
| 2.0   | 188  | 3.5261        | -                   |
| 3.0   | 282  | 3.4558        | -                   |
| 4.0   | 376  | 3.4149        | -                   |
| 5.0   | 470  | 3.3786        | -                   |
| 6.0   | 564  | 3.3552        | -                   |
| 7.0   | 658  | 3.3412        | -                   |
| 8.0   | 752  | 3.3241        | -                   |
| 9.0   | 846  | 3.3293        | -                   |
| 10.0  | 940  | 3.3131        | -                   |
| -1    | -1   | -             | 0.5968              |


### Training Time
- **Training**: 54.7 minutes

### Framework Versions
- Python: 3.14.4
- Sentence Transformers: 6.1.0
- Transformers: 5.17.0
- PyTorch: 2.14.0+cu130
- Accelerate: 1.15.0
- Datasets: 5.0.1
- Tokenizers: 0.23.2

## Additional Resources

- [Training and Finetuning Embedding Models with Sentence Transformers](https://huggingface.co/blog/train-sentence-transformers): the end-to-end guide for training or finetuning Sentence Transformer models.
- [Introduction to Matryoshka Embedding Models](https://huggingface.co/blog/matryoshka): variable-size embeddings that can be truncated with minimal quality loss.
- [Binary and Scalar Embedding Quantization for Significantly Faster & Cheaper Retrieval](https://huggingface.co/blog/embedding-quantization): post-training compression of embedding vectors.
- [Multimodal Embedding & Reranker Models with Sentence Transformers](https://huggingface.co/blog/multimodal-sentence-transformers): use text, image, audio, and video models through the same API.
- [Training and Finetuning Multimodal Embedding & Reranker Models with Sentence Transformers](https://huggingface.co/blog/train-multimodal-sentence-transformers): train multimodal embedding models, with a Visual Document Retrieval walkthrough.

## Citation

### BibTeX

#### Sentence Transformers
```bibtex
@inproceedings{reimers-2019-sentence-bert,
    title = "Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks",
    author = "Reimers, Nils and Gurevych, Iryna",
    booktitle = "Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing",
    month = "11",
    year = "2019",
    publisher = "Association for Computational Linguistics",
    url = "https://arxiv.org/abs/1908.10084",
}
```

#### MultipleNegativesRankingLoss
```bibtex
@misc{oord2019representationlearningcontrastivepredictive,
      title={Representation Learning with Contrastive Predictive Coding},
      author={Aaron van den Oord and Yazhe Li and Oriol Vinyals},
      year={2019},
      eprint={1807.03748},
      archivePrefix={arXiv},
      primaryClass={cs.LG},
      url={https://arxiv.org/abs/1807.03748},
}
```

<!--
## Glossary

*Clearly define terms in order to be accessible across audiences.*
-->

<!--
## Model Card Authors

*Lists the people who create the model card, providing recognition and accountability for the detailed work that goes into its construction.*
-->

<!--
## Model Card Contact

*Provides a way for people who have updates to the Model Card, suggestions, or questions, to contact the Model Card authors.*
-->