#!/usr/bin/env bash


function a() {
    echo "i am a"
}

function b() {
    echo "i am b"
}

function c() {
    a
    b
}

c