# cloudcoil.models.sealed_secrets

Typed sealed-secrets resources for the Cloudcoil Kubernetes client.

[![PyPI](https://img.shields.io/pypi/v/cloudcoil.models.sealed_secrets.svg)](https://pypi.org/project/cloudcoil.models.sealed_secrets/)
[![CI](https://github.com/cloudcoil/models-sealed-secrets/actions/workflows/ci.yml/badge.svg)](https://github.com/cloudcoil/models-sealed-secrets/actions/workflows/ci.yml)

## Install a published release

Requires Python 3.14+:

```sh
uv add cloudcoil.models.sealed_secrets
# Or:
pip install cloudcoil.models.sealed_secrets
```

Select a version matching the upstream APIs you use and pin a compatible Cloudcoil
minor. The [versioning guide](https://github.com/cloudcoil/cloudcoil/blob/main/VERSIONING.md)
explains the upstream version and packaging revision. Model installation does not
install Kubernetes or an upstream operator.

Use the [Cloudcoil documentation](https://cloudcoil.github.io/cloudcoil/) for client
operations, controllers and admission. Report generation or packaging problems in
[cloudcoil/cloudcoil](https://github.com/cloudcoil/cloudcoil/issues).

Licensed under [Apache-2.0](https://github.com/cloudcoil/cloudcoil/blob/main/LICENSE).
## Sealed Secrets models

Models are generated from pinned upstream schemas. Configuration, schema inputs
and README sources are maintained in
[cloudcoil/cloudcoil](https://github.com/cloudcoil/cloudcoil/tree/main/models/sealed-secrets);
the generated package is in
[cloudcoil/models-sealed-secrets](https://github.com/cloudcoil/models-sealed-secrets). Edit the
source integration in Cloudcoil because generated repository edits are replaced
on template refresh.

### Use a typed resource

After installing `cloudcoil.models.sealed_secrets`, use the package's typed lookup to
select an exact Kubernetes kind and API version:

```python
from cloudcoil.models.sealed_secrets import get_model

SealedSecret = get_model("SealedSecret", api_version="bitnami.com/v1alpha1")

for resource in SealedSecret.list(namespace="default"):
    print(resource.name)
```

The lookup is local; `list` reads the configured cluster. Async code uses
`await SealedSecret.async_list(namespace="default")`. Direct class imports are also supported; the
lookup avoids depending on schema-derived module names.

Install the upstream Sealed Secrets CRDs and operator separately before making API calls.
The model package supplies Python types and client methods, not the operator.

Use the shared [resource guide](https://cloudcoil.github.io/cloudcoil/resources/)
for constructors, builders, writes and watches, and the
[controller guide](https://cloudcoil.github.io/cloudcoil/controllers/) for
reconciliation. Pydantic validates constructed models at runtime; generated
annotations provide field completion and static type checking.

### Maintain this integration

From the Cloudcoil repository root:

```sh
make gen-repo-sealed-secrets
make -C output/models-sealed-secrets lint test check-artifacts
```

Rendering generates the models before validation. The
[model release guide](https://cloudcoil.github.io/cloudcoil/model-releases/)
covers source updates, artifact checks and publishing.
