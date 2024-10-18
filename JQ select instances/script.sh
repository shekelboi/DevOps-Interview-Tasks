#!/usr/bin/env bash

# TODO: Add the InstanceId to the output (with a key called `id`)
# TODO: Only return the Name tag, not all of them. (One row per instance))
# TODO: Make sure all instances are shown, even if it doesn't have a Name tag.

function list_all_ec2s_with_optional_name() {
  jq -c -r '.' data.json
}

list_all_ec2s_with_optional_name
