
# plnpt

    import plnpt
    
    tokens = plnpt.tokenizer("A Maria tem razão .")
    # ['A', 'Maria', 'tem', 'razão', '.']
    
    tags = plnpt.tagger("A Maria tem razão .")
    # [['A', 'o', 'DA0FS0', '0.675415'], ['Maria', 'maria', 'NCFS000', '1'], ['tem', 'ter', 'VMIP3S0', '0.999287'], ['razão', 'razão', 'NCFS000', '0.65'], ['.', '.', 'Fp', '1']]

    deps = plnpt.dep_parser("A Maria tem razão .")
    # [['1', 'A', '_', 'DET', 'art|<artd>|F|S', 'Definite=Def|Gender=Fem|Number=Sing|PronType=Art|fPOS=DET++art|<artd>|F|S', '2', 'det', '_', '_'], ['2', 'Maria', '_', 'PROPN', 'prop|F|S', 'Gender=Fem|Number=Sing|fPOS=PROPN++prop|F|S', '3', 'nsubj', '_', '_'], (...) ]

