<?php

class TestHTML extends \PHPFUI\HTMLUnitTester\Extensions
{
  public function testValidHtml()
  {
    $this->assertValidHtml('<h1>Header</h1>');
    $this->assertValidHtmlPage('<!DOCTYPE html><html><head><meta charset="utf-8"/><title>Title</title></head><body><div>This is a test</div></body></html>');
  }
  public function testValidCssFile(): void
  {
    $this->assertValidCssFile(getcwd() . "/src/exemple1.css");
  }
  public function testValidFile(): void
  {
    $this->assertValidFile(getcwd() . "/src/exemple1.html");
  }
}
